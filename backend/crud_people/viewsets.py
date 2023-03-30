from rest_framework import viewsets
from crud_people.models import Person
from crud_people.serializers import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()
