from django.urls import re_path as url
from django.urls import include, path
from .views import *


from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('companies', CompanyViewSet)
router.register('categories', CategoryViewSet)
router.register('facilities', FacilityViewSet)

router.register('search', SearchViewSet, basename='Benefits')


urlpatterns = router.urls