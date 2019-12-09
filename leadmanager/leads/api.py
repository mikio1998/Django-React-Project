# Creating the api

from leads.models import Lead 
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer


# A viewset allows us to create a full CRUD Api, without 
# having to specify specific methods for functionality.
# CRUD Api: create read update delete

# Viewset combines the logic for a set of 
# related views in a single class.

# Lead Viewset
class LeadViewSet(viewsets.ModelViewSet):
	# query that grabs all the leads
	queryset = Lead.objects.all()

	permission_classes = [
		permissions.AllowAny
	]

	serializer_class = LeadSerializer







