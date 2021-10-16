from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, GroupViewSet, TicketViewSet, CurrentUserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'current-user', CurrentUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
