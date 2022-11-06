from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

app_name = 'main_app'

router = SimpleRouter()
router.register('users', views.UserViewSet)
router.register('riders', views.RiderViewSet)
router.register('drivers', views.DriverViewSet)

urlpatterns = [
    path('', include(router.urls))
]