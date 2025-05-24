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
  "total_revenue": 3814.4635
}
```


### Updates and Imports - Using Cron - Django Management Command

- All data can be imported and updated via a single import script
- Best practice would be isolated functionality 
