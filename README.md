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

### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pip install -r requirements.txt
    
      
      
After that just install the local dependencies, run migrations, and start the server.

Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

## 🌐 API Endpoints

| Endpoint | Query Parameters | Response Example |
|----------|------------------|------------------|
| `/revenue` | `start_date=YYYY-MM-DD`<br>`end_date=YYYY-MM-DD` | `{ "total_revenue": <total revenue> }` |
| `/revenue` | `start_date=YYYY-MM-DD`<br>`end_date=YYYY-MM-DD`<br>`product_id=#`<br>`category=#`<br>`region=#` | `{ "total_revenue": <total revenue> }` |

---

### Example

```bash
GET /revenue?start_date=2024-01-01&end_date=2024-12-31
```

### Updates and Imports - Using Cron - Django Management Command

- All data can be imported and updated via a single import script
- Best practice would be isolated functionality 


### Please Note:
- I couldn't complete the import script or test the system completely in the stipulated time. :(