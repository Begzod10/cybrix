from rest_framework.routers import DefaultRouter

from client_requests.api.crud import ClientRequestViewSet

router = DefaultRouter()
router.register(r'client-requests', ClientRequestViewSet, basename='client-request')

urlpatterns = router.urls
