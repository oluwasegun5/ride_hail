from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

app_name = 'main_app'

router = SimpleRouter()
router.register('users', views.UserViewSet)
router.register('riders', views.RiderViewSet)
router.register('drivers', views.DriverViewSet)
router.register('cards', views.CardViewSet)
router.register('rides', views.RideViewSet)
router.register('reviews', views.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls))
]