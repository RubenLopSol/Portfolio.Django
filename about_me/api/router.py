from rest_framework.routers import DefaultRouter
from about_me.api.views import About_meApyViewset


router_about_me = DefaultRouter()
router_about_me.register(
    prefix= 'about_me', basename= 'about_me', viewset= About_meApyViewset
)