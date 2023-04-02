from crud_people.models import Person
from crud_people.serializers import PersonSerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from json import JSONDecodeError

class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()
    
    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = PersonSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
                return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)

    def delete(request, id):
        data = get_object_or_404(Person, id=id) 
        data.delete()
        return Response(status = status.HTTP_200_OK)
    