# W/ rest framework we create serializer

# Serializers allow complex data such as 
# querysets and model instances to be converted 
# to native Python datatypes that can then 
# be easily rendered into JSON, XML or 
# other content types.
# 
# We need to use serializer to take our 
# Model or queryset of leads and turn it 
# into JSON.

#


from rest_framework import serializers
from leads.models import Lead

# Lead Serializer
# Turning our Lead model into a seralizer,
# or creating one from it. 
class LeadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lead
		fields = '__all__' 
		














