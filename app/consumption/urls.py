from django.urls import path, include
from rest_framework.routers import DefaultRouter

from consumption import views


router = DefaultRouter()
router.register("consumption_types", views.Consumption_typeViewSet)

app_name = "consumption"

urlpatterns = [path("", include(router.urls))]
