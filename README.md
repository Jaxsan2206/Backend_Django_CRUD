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
    'pokemon.apps.PokemonConfig',
    # etc... 
]
```
* To create a base route path for all your pokemon routes, you need to add the following in the urls.py in the server folder. 

```
# shelter/urls.py
from django.contrib import admin # this is in by default
from django.urls import path, include # importing include as well as path

urlpatterns = [
    path('pokemon/', include('pokemon.urls')), # add pokemon urls
    path('admin/', admin.site.urls), # this is in by default, visit :8000/admin to see
]
```
If you'd prefer to not have /pokemon/ as part of your route, you can simply leave the path as an empty string.

*  After you set up the base route, you can create a urls.py file in the pokemon app folder such as the following: 

```
from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index), 
    path('<int:id>', views.show)
]
```
* Create some models like the below: 
```
from django.db import models
from django.core import serializers

# Create your models here.
class Pokemon(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.name
```
* After creating the model, run `python manage.py makemigrations pokemon` 
* then you can run those migrations with `python manage.py migrate`
* Everytime the models.py file is updated, the 2 commands above are ran.
* If you wish to interact with the database, then you need to enter the shell using `python manage.py` and then import the model using `from pokemon.models import Pokemon` 

Create
* gh = Breed(name='Greyhound', temperament='kind, gentle') make new instance
* gh.save() persist new instance as db record
* gh.dog_set.create(name='Zozo', age=4) make a new Dog record with a breed of greyhound

Read
* Dog.objects.all() see all records
* Dog.objects.first() see first record
* Dog.objects.get(pk=2) get record by id
* Dog.objects.filter(name='Mochi') find all dogs with name 'Mochi'
* Dog.objects.filter(breed_name='greyhound') find all dogs with breed of name 'greyhound'

Update
* b = Breed.objects.get(pk=2) get breed with id 2
* b.temperament='extra snuggly' update temperament field
* b.save() save changes

Destroy
* b.delete()

* To create an admin user and use the admin panel (comes in a default Django setup at /admin), you will need to create a super user using `python manage.py createsuperuser`. 
* Visit /admin and log in with your new credentials.
* To add a model to your admin, register it in your `<app-name>/admin.py`

```
# adoption/admin.py
from django.contrib import admin

# Register your models here.
from .models import Pokemon
admin.site.register(Pokemon)
```