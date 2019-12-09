
# include:
# A function that takes a full Python import path 
# to another URLconf module that should 
# be “included” in this place.

from django.contrib import admin
# include: so you can include separate files.
from django.urls import path, include

urlpatterns = [
    path('', include('leads.urls')),
]







