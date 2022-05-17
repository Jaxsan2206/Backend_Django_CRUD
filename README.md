# Workflow 

* `pipenv shell`
* `pipenv install Django`
* `django-admin startproject server`
* cd into the server folder and run `python manage.py runserver`
* You can create an app using `python manage.py startapp <app-name>`. 
* After creating an app, you need to update the settings.py 

```
# shelter/settings.py
INSTALLED_APPS = [
    # <appname>.apps.<AppConfigClass>
    'adoptions.apps.AdoptionConfig',
    # etc... 
]
```
* `pipenv shell`
* `pipenv shell`
* `pipenv shell`

