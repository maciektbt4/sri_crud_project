from django.urls import path
from .viewsets import PersonViewSet, CarViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'person', PersonViewSet, basename='person')
router.register(r'car', CarViewSet, basename='car')
urlpatterns = router.urls
urlpatterns += [
    path('person/<int:person_id>/remove_car/<int:car_id>/', PersonViewSet.as_view({'post': 'remove_car'}), name='person-remove-car'),
    path('car/<int:car_id>/add_owner/<int:owner_id>/', CarViewSet.as_view({'post': 'add_owner'}), name='car-add-owner'),

]