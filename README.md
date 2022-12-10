# Radeband
Radeband is a open-source python project that presents the companies facilities for their employees. We believe that employees deserve more.

## Migrations
Delete your database (db.sqlite3 in my case) in your project directory
Remove everything from __pycache__ folder under your project subdirectory
For the application you are trying to fix, go to the folder and clear migrations and __pycache__ directories
```
python manage.py makemigrations
python manage.py migrate
```

## Run the app
python manage.py runserver


## Create Super User
python manage.py createsuperuser