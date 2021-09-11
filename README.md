# Django_app

### Built with Python(Django Framework) And Bootstrap 
* [Bootstrap](https://getbootstrap.com)
* [Django](https://www.djangoproject.com/)

### Prerequisites
* python
* pip

### Installation
1. Download PostgresSql data base and PGADMIN GUI for database.
2. using defau/t daabse. postgres
3. update website/settings.py with postgreas password

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER' : 'postgres',
            'PASSWORD' : '', #add password
            'HOST' : 'localhost'
        }
    }
4. Goto project root folder iniside django_app/project/website
5. create virtual env
    ```sh
    python -m venv env
   ```

6. Activate virtual env
    Inside a project root directory (django_app/project/website)
    ```sh
    env\Scripts\activate
    ```

7. Install requirements
    ```sh
    pip install -r requirements.txt
    ```
    (env) <projectlocation>\django_app\project\website>pip install -r requirements.txt

8. Run DB migrtations
    (env) <projectlocation>\django_app\project\website>python manage.py migrate

9. Collect static files
    (env) <projectlocation>\django_app\project\website>python manage.py collectstatic

10. Upload CSV file in to database table
    (env) <projectlocation>\django_app\project\website>python manage.py runscript scripts.csv_import

## Run the application
(env) <projectlocation>\django_app\project\website>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 10, 2021 - 14:08:21
Django version 3.2.7, using settings 'website.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

Open http://127.0.0.1:8000/ to search for websites from database


## create super user for application

(env) <projectlocation>\django_app\project\website>python manage.py runserver
Username (leave blank to use 'admin'): admin
Email address:admin@mail.com
Password:
Password (again):
Bypass password validation and create user anyway? [y/N]:y


## For super user login
1. Open http://127.0.0.1:8000/admin