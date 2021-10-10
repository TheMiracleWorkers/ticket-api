from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, GroupViewSet, TicketViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'tickets', TicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
