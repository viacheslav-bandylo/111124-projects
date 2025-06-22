# 🖥 Django project backend dev


## 🏫 **This is a project written during studying in IT Career Hub**
p.s. you can also use this backend structure for your website.

---

## 🗂 Structure of project

```
django_prod/
    ├── app/
    │    ├── migrations/
    │            ├── __init__.py
    │            └── 0001_initial.py
    │    ├── __init__.py
    │    ├── admin.py
    │    ├── apps.py
    │    ├── models.py
    │    ├── tests.py
    │    ├── urls.py
    │    └── views.py
    ├── autotests/
    │    └── autoqa.py
    ├── config/
    │    ├── __init__.py
    │    ├── asgi.py
    │    ├── settings.py
    │    ├── urls.py
    │    └── wsgi.py
    ├── library
    │    ├── migrations/
    │            ├── __init__.py
    │            └── 0001_initial.py
    │    ├── __init__.py
    │    ├── admin.py
    │    ├── apps.py
    │    ├── models.py
    │    ├── tests.py
    │    ├── urls.py
    │    └── views.py
    ├── project/
    │    ├── migrations/
    │            ├── __init__.py
    │            ├── 0001_initial.py
    │            ├── 0002_rename_title_project_name_alter_project_lang.py
    │            ├── 0003_alter_developer_project_alter_project_lang_and_more.py
    │            ├── 0004_alter_developer_project_alter_project_lang_and_more.py
    │            ├── 0005_alter_project_lang.py
    │            ├── 0006_alter_project_lang.py
    │            ├── 0007_rename_lang_project_language.py
    │            ├── 0008_alter_project_language.py
    │            ├── 0009_alter_project_language.py
    │            ├── 0010_alter_project_language.py
    │            ├── 0011_alter_project_language.py
    │            ├── 0012_alter_project_language.py
    │            ├── 0013_alter_project_language.py
    │            └── 0014_alter_project_language.py
    │    ├── __init__.py
    │    ├── admin.py
    │    ├── apps.py
    │    ├── models.py
    │    ├── tests.py
    │    ├── urls.py
    │    └── views.py
    ├── TaskManager/
    │    ├── migrations/
    │            ├── __init__.py
    │            ├── 0001_initial.py
    │            ├── 0002_alter_category_options_alter_subtask_options_and_more.py
    │            ├── 0003_alter_subtask_deadline_alter_task_deadline.py
    │            ├── 0004_alter_subtask_deadline_alter_task_deadline.py
    │            ├── 0005_remove_task_unique_task_title_date_remove_task_date_and_more.py
    │            ├── 0006_alter_subtask_deadline_alter_task_deadline.py
    │            ├── 0007_alter_subtask_deadline_alter_task_deadline.py
    │            ├── 0008_alter_subtask_deadline_alter_task_deadline.py
    │            └── 0009_alter_subtask_deadline_alter_task_deadline.py
    │    ├── __init__.py
    │    ├── admin.py
    │    ├── apps.py
    │    ├── models.py
    │    ├── tests.py
    │    ├── urls.py
    │    └── views.py
    ├── .gitignore
    ├── README.md
    ├── manage.py
    └── requirements.txt
```

---

## 🛠 **What do you need to install this project on your PC?**
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

---

## ⚙️ Tech stack / requirements
```
▪️Django
▪️django-environ
▪️pytest
▪️python-dotenv
▪️selenium
▪️sqlparse
▪️and some other additional reqs
```
