from rest_framework.routers import DefaultRouter

from .views import LanguageProgramming, FrameworkViewSet, DatabaseViewSet

router = DefaultRouter()
router.register(r'languages', LanguageProgramming, basename='languages')
router.register(r'frameworks', FrameworkViewSet, basename='frameworks')
router.register(r'database', DatabaseViewSet, basename='database')

urlpatterns = router.urls
