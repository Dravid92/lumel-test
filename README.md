# lumel-test

### Prerequisites

- Python 3.10+
- pip
- Virtualenv (optional but recommended)
- PostgreSQL/MySQL/SQLite (based on your project)

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