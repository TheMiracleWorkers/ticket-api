from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, RoleViewSet, TicketViewSet, CurrentUserViewSet, RegisterViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'current-user', CurrentUserViewSet)
router.register(r'register', RegisterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
