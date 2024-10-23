from rest_framework.routers import DefaultRouter

from projects.api.crud import ProjectViewSet

router = DefaultRouter()
router.register(r'project', ProjectViewSet, basename='project')

urlpatterns = router.urls
