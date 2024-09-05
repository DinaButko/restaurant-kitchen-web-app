# How to set up django project
1. pip install django
2. django-admin startproject mysite . # create django project, create dir with default files mysite
3. python manage.py startapp restaurant_menu # creates  a new directory, this is app
4. in mysite/settings.py add in INSTALLED_APPS ->  "restaurant_menu"
5. python manage.py runserver # command to run server
6. build database model (models.py)
7. create database python manage.py makemigrations
8. python manage.py migrate # created database and we can open it in SQL3Lite
9. work on views.py # to get data data from database model and show it in html form 
10. create folder templates and add html files
11. connect views to html files (views.py) + url part
12. in restarurant_menu.py create url.py file 
13. in mysite/urls.py add  path('', include('restaurant_menu.urls'))
14. context in django, e.x. # 'meals' we will use in index.html, e.x. <h3>{{ meals}}</h3>
        context = {"meals": "Pizza", "ingredients": ["things"]}
15. create admin interface restaurant_menu/admin.py
16. create admin:  python manage.py createsuperuser: u: admin@admin.com p: admin

