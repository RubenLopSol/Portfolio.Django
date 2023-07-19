from rest_framework.routers import DefaultRouter
from education.api.views import EducationApyViewset


router_education = DefaultRouter()
router_education.register (
    prefix= 'education', basename= 'education', viewset= EducationApyViewset
) 