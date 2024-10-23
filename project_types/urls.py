from rest_framework.routers import DefaultRouter

from .views import ProjectTypeViewSet

router = DefaultRouter()
router.register(r'project-type', ProjectTypeViewSet, basename='project-type')

urlpatterns = router.urls
