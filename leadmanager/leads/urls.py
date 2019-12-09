# Instead of creating explicit paths 
# in urls.py (leadmanager), we will use the router from
# rest framework.
# 
# REST framework adds support for automatic URL routing 
# to Django, and provides you with a simple, 
# quick and consistent way of wiring your view logic 
# to a set of URLs.


from rest_framework import routers
from .api import LeadViewSet


router = routers.DefaultRouter()
# Register routes to router
# endpoint: 'api/leads'
router.register('api/leads', LeadViewSet, 'leads')


# Instead of listing paths in urlpatterns 
# in urls.py (leadmanager)...
# This will give us the urls that are registered to 
# 'api/leads' endpoint.
urlpatterns = router.urls







