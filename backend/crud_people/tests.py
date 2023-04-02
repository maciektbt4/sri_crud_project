from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Person

class PersonTestCase(APITestCase):

    """
    Test suite for Contact
    """
    def setUp(self):
        self.client = APIClient()
        self.data = {
            "sex": "Male",
            "first_name": "billy",
            "last_name": "smith",
            "job": "software engineer",
            "email": "billysmith@test.com",
        }
        self.url = "/person/"
        
    def test_create_person(self):
        '''
        test PersonViewSets create method
        '''
        data = self.data
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.get().first_name, "billy")
        self.assertEqual(Person.objects.get().email, "billysmith@test.com")
    
    def test_get_person_list(self):
        '''
        test PersonViewSets get method
        '''
        data = self.data

        "Create 10 objects in loop"
        for i in range (0,10):
            self.client.post(self.url, data)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Person.objects.count(), 10)
    
    def test_delete_person(self):
        person  = Person.objects.create(sex = "male", first_name = "jan",
                                        last_name = "kowalski", job = "software eng",
                                        email= "ksl@jk.com" )
        pk = person.pk
        delete_url = self.url + "/" + str(pk) + "/"
        
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Person.objects.count(), 0)