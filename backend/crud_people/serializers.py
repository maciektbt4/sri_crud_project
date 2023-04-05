from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField
from crud_people.models import Person
from datetime import date

class PersonSerializer(serializers.ModelSerializer):
	email = serializers.EmailField()
	birth_date = serializers.DateField()

	def validate_birth_date(self,birth_date):
		earliest_brith_date = date(1900,1,1)
		if birth_date < earliest_brith_date:
			raise serializers.ValidationError('Birth_date must be greather than 1900-01-01.')
		return birth_date
	
	class Meta:
		model = Person
		fields = ['id', 'sex', 'first_name', 'last_name', 'job', 'email', "birth_date"]

