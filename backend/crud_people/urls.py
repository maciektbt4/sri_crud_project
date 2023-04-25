from .viewsets import PersonViewSet, HobbyViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'person', PersonViewSet, basename='person')
router.register(r'hobby', HobbyViewSet, basename='hobby')
urlpatterns = router.urls