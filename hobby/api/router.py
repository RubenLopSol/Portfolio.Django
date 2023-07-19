from rest_framework.routers import DefaultRouter
from hobby.api.views import HobbyApyViewset


router_hobby = DefaultRouter()
router_hobby.register(
    prefix= 'hobby', basename= 'hobby', viewset= HobbyApyViewset
)