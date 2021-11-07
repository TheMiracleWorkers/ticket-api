from django.urls import path, include
from rest_framework_nested import routers

from .views import UserViewSet, GroupViewSet, TicketViewSet, CurrentUserViewSet, ProjectViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'current-user', CurrentUserViewSet)

projects_router = routers.NestedSimpleRouter(
    router, 'projects', lookup='project')
projects_router.register('tickets', TicketViewSet, basename='project-tickets')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(projects_router.urls)),
]
