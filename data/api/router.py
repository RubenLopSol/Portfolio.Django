from rest_framework.routers import DefaultRouter
from data.api.views import DataApyViewset

router_data = DefaultRouter()
router_data.register (
    prefix= 'data', basename= 'data', viewset= DataApyViewset
)