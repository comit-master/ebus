Website built with django-python javascript from scratch

1. Create Website 

2. Install psycopg, gunicorn, django-heroku, dj_database_url

3. Create a file runtime.txt

4. Create the Procfile file 

5. Generate the requirements.txt file >> pip freeze > requirements

6. Push the project on GITHUB

7. Create an heroku account 

8. Download Heroku Cli
	https://devcenter.heroku.com/articles/heroku-cli

9. Configurate django heroku

10. Configurate whitenoise 
	https://whitenoise.evans.io/en/stable/django.html

10. Heroku comman to login and push the website to heroku server 
	git init 
	git add .
	git commit -m"update settings to deploy"
	heroku login 
	heroku create website
	git push heroku master 
	heroku run python manage.py migrate
	heroku open



Requirements 
astroid==2.4.2
certifi==2020.12.5
chardet==4.0.0
colorama==0.4.4
distlib==0.3.4
dj-database-url==0.5.0
django-cors-headers==3.4.0
django-filter==21.1
djangorestframework==3.12.2
ecom==1.1.1
elasticsearch==7.12.0
filelock==3.6.0
greenlet==1.1.2
idna==2.10
isort==5.7.0
lazy-object-proxy==1.4.3
mccabe==0.6.1
mysqlclient==2.1.0
numpy==1.20.2
olefile==0.46
pandas==1.2.4
pi==0.1.2
Pillow==8.0.0
platformdirs==2.5.2
pydantic==1.9.0
PyJWT==1.7.1
pylint==2.6.0
python-dateutil==2.8.1
pytz==2021.1
requests==2.25.1
six==1.15.0
SQLAlchemy==1.4.36
toml==0.10.2
typing-extensions==4.2.0
urllib3==1.26.4
virtualenv==20.14.1
wrapt==1.12.1
dj-database-url==0.5.0
Django==4.0.4
django-heroku==0.3.1
gunicorn==20.1.0
psycopg2==2.9.3
sqlparse==0.4.2
tzdata==2022.1
whitenoise==6.1.0
