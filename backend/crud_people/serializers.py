from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField
from crud_people.models import Person

class PersonSerializer(serializers.ModelSerializer):
	email = serializers.EmailField()
	
	class Meta:
		model = Person
		fields = ['id', 'sex', 'first_name', 'last_name', 'job', 'email']