from .viewsets import PersonViewSet, CarViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'person', PersonViewSet, basename='person')
router.register(r'car', CarViewSet, basename='car')
urlpatterns = router.urls