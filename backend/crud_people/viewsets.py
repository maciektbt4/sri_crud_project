from rest_framework.decorators import action
from crud_people.models import Person, Car
from crud_people.serializers import PersonSerializer, CarSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class PersonViewSet(viewsets.ViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
   
    #get all
    def list(self, request):
        queryset = Person.objects.all()
        serializer = PersonSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #get one by id
    def retrieve(self, request, pk=None):
        queryset = Person.objects.all()
        # queryset = queryset.prefetch_related('car_set')
        person = get_object_or_404(queryset, pk=pk)
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
        queryset = Person.objects.all()
        person=get_object_or_404(queryset, pk=pk)
        person.delete()
        return Response({'msg':f'Person datas with id = {pk} is deleted'}, status=status.HTTP_200_OK)           

    #put update one by id    
    def update(self, request, pk=None):
        try:
            person = Person.objects.get(pk = pk)  
            serializer=PersonSerializer(person, data=request.data)
        except:
            serializer=PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    #patch partial (not all fields required in request) update one by id    
    def partial_update(self, request, pk=None):
        queryset = Person.objects.all()
        person=get_object_or_404(queryset, pk=pk)
        serializer=PersonSerializer(person, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    #Exercise 3: return all cars from defined owner- custom url
    @action(detail=True, methods=['get'])
    def cars(self, request, pk=None):
        cars = Car.objects.all()        
        cars_person_owned = cars.filter(owner = pk)
           
        try:
            Person.objects.get(id=pk)
        except Person.DoesNotExist:
            return Response(f"Person with id = {pk} is not found", status=status.HTTP_404_NOT_FOUND)

        serializer = CarSerializer(cars_person_owned, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'], url_path='remove_car/(?P<car_id>[^/.]+)')
    def remove_car(self, request, pk=None, car_id=None):
        try:
            car = Car.objects.get(pk = car_id, owner = pk)
            car.owner = None
            car.save()
            return Response(CarSerializer(car).data, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    @action(detail=True, methods=['post'], url_path='add_owner/(?P<owner_id>[^/.]+)')
    def add_owner(self, request, pk=None, owner_id=None):
        try:
            car = Car.objects.get(pk=pk)
            person = Person.objects.get(pk=owner_id)
            car.owner = person
            car.save()
            return Response(CarSerializer(car).data, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def remove_owner(self, request, pk=None):
        try:
            car = Car.objects.get(pk=pk)
            car.owner = None
            car.save()
            return Response(CarSerializer(car).data, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
