from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoleViewSet, CourseNodeViewSet, UserProgressViewSet

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'roles', RoleViewSet, basename='role')
router.register(r'courses', CourseNodeViewSet, basename='coursenode')
router.register(r'progress', UserProgressViewSet, basename='userprogress')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]