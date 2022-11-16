from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('v1/hailride/', include('main_app.urls', namespace='main_app')),
    path('^auth/', include('djoser.urls')),
    path('^auth/', include('djoser.urls.jwt')),
]
