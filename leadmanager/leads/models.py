# Models contains the essential fields 
# and behaviors of the data you’re storing.

# After making changes in models...
# $ python manage.py makemigrations (appname)
# $ python manage.py migrate

from django.db import models

# Pass in models.Model, to use some of the objects from
# the core model class. 
class Lead(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100, unique=True)
	message = models.CharField(max_length=500, blank=True) #blank=True to make it optional
	created_at = models.DateTimeField(auto_now_add=True) # automatically add date.
