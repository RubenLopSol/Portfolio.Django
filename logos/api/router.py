from rest_framework.routers import DefaultRouter
from logos.api.views import LogosApyViewset


router_logos = DefaultRouter()
router_logos.register (
    prefix='logos', basename='logos', viewset=LogosApyViewset
)