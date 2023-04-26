from rest_framework import serializers
from crud_people.models import Person, Car
from datetime import date

class CarSerializer(serializers.ModelSerializer):
	year = int
	def validate_year(self,year):
		earliest_construction_year = 1886
		if year < earliest_construction_year or year > date.today().year:
			raise serializers.ValidationError('Construction year must be greather than 1886 and smaller or equal this year.')
		return year
	class Meta:
		model = Car
		fields = ['id','plate','make','model', 'year', 'owner']

class PersonSerializer(serializers.ModelSerializer):
	cars = CarSerializer(many=True, read_only=True)
	email = serializers.EmailField()
	birth_date = serializers.DateField()

	def validate_birth_date(self,birth_date):
		earliest_brith_date = date(1900,1,1)
		if birth_date < earliest_brith_date or birth_date > date.today():
			raise serializers.ValidationError('Birth_date must be greather than 1900-01-01 and smaller or equal today.')
		return birth_date
	
	class Meta:
		model = Person
		fields = ['id', 'sex', 'first_name', 'last_name', 'job', 'email', 'birth_date', 'cars']

