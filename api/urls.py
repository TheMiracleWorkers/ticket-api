from django.urls import path, include
from rest_framework_nested import routers

from .views import StatusViewSet, UserViewSet, RoleViewSet, TicketViewSet, CurrentUserViewSet, RegisterViewSet, ProjectViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'status', StatusViewSet)
router.register(r'current-user', CurrentUserViewSet)
router.register(r'register', RegisterViewSet)

projects_router = routers.NestedSimpleRouter(
    router, 'projects', lookup='project')
projects_router.register('tickets', TicketViewSet, basename='project-tickets')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(projects_router.urls)),
]
