from rest_framework.routers import DefaultRouter
from contact.api.views import ContactViewSet


router_contact = DefaultRouter()
router_contact.register (
    prefix= 'contact', basename= 'contact', viewset= ContactViewSet
) 