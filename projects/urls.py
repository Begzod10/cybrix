from rest_framework.routers import DefaultRouter

from projects.api.crud import ProjectViewSet, ProjectDocumentsViewSet

router = DefaultRouter()
router.register(r'project', ProjectViewSet, basename='project')
router.register(r'project-documents', ProjectDocumentsViewSet, basename='project-documents')

urlpatterns = router.urls
