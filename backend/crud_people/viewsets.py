from crud_people.models import Person
from crud_people.serializers import PersonSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class PersonViewSet(viewsets.ViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    #get all
    def list(self, request):
        serializer = PersonSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #get one by id
    def retrieve(self, request, pk=None):
        person = get_object_or_404(self.queryset, pk=pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #put create
    def create(self,request):
        serializer=PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    #delete one by id
    def destroy(self, request,pk): 
        person=get_object_or_404(self.queryset, pk=pk)
        person.delete()
        return Response({'msg':f'Person datas with id = {pk} is deleted'}, status=status.HTTP_200_OK)           

    #put update one by id    
    def update(self, request, pk=None):
        person=get_object_or_404(self.queryset, pk=pk)
        serializer=PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    #patch partial (not all fields required in request) update one by id    
    def partial_update(self, request, pk=None):
        person=get_object_or_404(self.queryset, pk=pk)
        serializer=PersonSerializer(person, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
