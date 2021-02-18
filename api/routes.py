from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

from rest_framework.schemas import get_schema_view

from rest_framework.renderers import CoreJSONRenderer

routers = DefaultRouter()
routers.register("orgs", views.OrganizationViewSet)

urlpatterns = [path("", include(routers.urls))]
