from rest_framework.routers import DefaultRouter
from project.api.views import ProjectApyViewset


router_project = DefaultRouter()
router_project.register (
    prefix= 'project', basename= 'project', viewset= ProjectApyViewset
)