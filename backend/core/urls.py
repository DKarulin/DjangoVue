from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter

from core.views import CarViewSet
from core.views import UserViewSet

router = DefaultRouter()
router.register("cars", CarViewSet)
router.register("users", UserViewSet)

urlpatterns = router.urls
