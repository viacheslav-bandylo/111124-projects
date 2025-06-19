# Django project backend dev

---

## **This is a project written during studying in IT Career Hub**
p.s. you can also use this backend structure for your website.

---

## **What do you need to install this project on your PC?**
1. At first, you should load this repository to your PC:
    ```shell
    git clone git@github.com:grosspapatrn/django_prod.git
    ```
2. If you want to do any changes in this project, open in your IDE and go to files "_/models.py_"
3. Now you should create a file "_.env_", which should contain those all things:
   - SECRET_KEY=""
   - DEBUG=True / False
   - ALLOWED_HOSTS=[]

   ### Database connection
   - DB_ROUTER=False

   ### MySQL connection
   - MYSQL_ENGINE=
   - MYSQL_NAME=
   - MYSQL_USER=
   - MYSQL_PASSWORD=
   - MYSQL_HOST=
   - MYSQL_PORT=

   ### SQLite connection
   - SQLITE_ENGINE=
   - SQLITE_NAME=
   
4. If you continue with all those settings, you should run those commands:
    ```shell
    python manage.py makemigrations
    ```
    ```shell
    python manage.py migrate
    ```
    ```shell
    python manage.py createsurperuser
    ```
5. If you did all those things, type this command:
    ```shell
    python manage.py runserver
    ```
    → and go to link below :) 