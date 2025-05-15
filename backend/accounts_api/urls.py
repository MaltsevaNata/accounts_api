from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from accounts import views

router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/', include(router.urls)),
]
