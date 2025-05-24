# lumel-test

### Prerequisites

- Python 3.10+
- pip
- Virtualenv 
- MySQL

---

### Getting Started

### Clone the repository

   ```
   git clone https://github.com/Dravid92/lumel-test.git
   cd lumel-test
   ```

### Set up virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is needed and before running the below commands make sure you are in the env.

run to install all requirements for the project:

    $ pip install -r requirements.txt
    
      
      
After that just install the local dependencies, run migrations, and start the server.

Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
- If the server is running fine , this should be coming up in the command line.

```
System check identified no issues (0 silenced).
May 24, 2025 - 11:44:03
Django version 5.2.1, using settings 'lumel.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
## Import Data

- In order import data you have to run the following command after running the migration
- This is the [excel sheet](https://docs.google.com/spreadsheets/d/16FlCbvqT15RvbIzbHKLVpV9aB0BxEE6g8eTWDX00WAM/edit?gid=1552958878#gid=1552958878) used to import data

```commandline
python manage.py import_sales.py
```
- The above command should return "all ok"
## Update Data 
- This same script can be used to update the data as well - this can be achieved by setting up a cron job in the server.
## API Endpoints

| Endpoint | Query Parameters | Description | Response Example |
|----------|------------------|-------------|------------------|
| `/revenue` | `start_date=YYYY-MM-DD`<br>`end_date=YYYY-MM-DD` | Get **Total Revenue** for a date range. | `{ "total_revenue": <amount> }` |
| `/revenue` | `start_date=YYYY-MM-DD`<br>`end_date=YYYY-MM-DD`<br>`product_id=<product_id>` | Get **Total Revenue by Product** for a date range. | `{ "total_revenue": <amount> }` |
| `/revenue` | `start_date=YYYY-MM-DD`<br>`end_date=YYYY-MM-DD`<br>`category=<category>` | Get **Total Revenue by Category** for a date range. | `{ "total_revenue": <amount> }` |
| `/revenue` | `start_date=YYYY-MM-DD`<br>`end_date=YYYY-MM-DD`<br>`region=<region>` | Get **Total Revenue by Region** for a date range. | `{ "total_revenue": <amount> }` |

---

### Example

```bash
GET /revenue?start_date=2024-01-01&end_date=2024-12-31

```
### Example

```bash
GET /revenue/?start_date=2023-12-15&end_date=2024-12-31
```
- Example Response
```
{
  "total_revenue": 3680.4635
}
```


### Updates and Imports - Using Cron & Django Management Command

- All data can be imported and updated via a single import script
- Best practice would be isolated functionality 


## Database Schema

### 1️. Customer


| Field Name | Data Type |
|------------|-----------|
| `id` | AutoField (Primary Key) |
| `name` | CharField (max_length=50) |
| `email` | EmailField |
| `address` | TextField |

---

### 2️.  Product

| Field Name | Data Type |
|------------|-----------|
| `id` | AutoField (Primary Key) |
| `name` | CharField (max_length=100) |
| `category` | CharField (max_length=100) |
| `unit_price` | DecimalField (max_digits=10, decimal_places=2) |
| `quantity` | IntegerField |
| `discount` | DecimalField (max_digits=5, decimal_places=2) |
| `shipping_cost` | DecimalField (max_digits=10, decimal_places=2) |
| `ref` | CharField (max_length=10) |

---

### 3️. Order

| Field Name | Data Type |
|------------|-----------|
| `id` | AutoField (Primary Key) |
| `date_of_sales` | DateField |
| `payment_method` | CharField |
| `region_of_sales` | CharField |
| `customer` | ForeignKey (to Customer) |
| `product` | ForeignKey (to Product) |
| `ref` | CharField (max_length=10) |

### Trade-Offs / Assumptions - DB Schema
- Its assumed that the customers are unique based off of email address 
- "ref" field is for the reference id of the order or the product connected to an order - for humans
- constraints for uniqueness and not mandatory ones are not added because of time constraints.

### Logic for Total Revenue Calculation
- For each sale the product associated with it is fetched to apply the below logic 
- The below formula was used to calculate the total sum , which was cumulatively added and returned. 
```
Total Revenue = (Quantity * Unit Price) - Discount Amount - Shipping Cost
```
```python
        discount = sale.product.discount
        discount_amount = sale.product.unit_price * discount
        total_revenue += (sale.product.quantity * sale.product.unit_price) - discount_amount - sale.product.shipping_cost
```