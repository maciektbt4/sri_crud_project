from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Person

class PersonTestCase(APITestCase):

    """
    Test suite for Person
    """
    def setUp(self):
        self.client = APIClient()
        self.data = {
            "sex": "Male",
            "first_name": "billy",
            "last_name": "smith",
            "job": "software engineer",
            "email": "billysmith@test.com",
            "birth_date": "2000-01-01"
        }
        self.partial_modified_data = {
            "first_name": "Julia",
            "last_name": "Gonzalez",
        }
        self.full_modified_data = {
            "sex": "Female",
            "first_name": "Julia",
            "last_name": "Gonzalez",
            "email": "jki@goole.com",
            "job": "Librarian",
            "birth_date": "2000-01-01"
        }
        self.url = "/person/"
        self.url_person_1 = "/person/1/"
            
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
    
    def test_update_person(self):
        '''
        test PersonViewSets update method
        '''
        PersonTestCase.test_create_person(self)

        response = self.client.put(self.url_person_1, self.partial_modified_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.put(self.url_person_1, self.full_modified_data)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.get().job, "Librarian")
        self.assertEqual(Person.objects.get().email, "jki@goole.com")   

    def test_partial_update_person(self):
        '''
        test PersonViewSets partial update method
        '''
        PersonTestCase.test_create_person(self)
        
        response = self.client.patch(self.url_person_1, self.partial_modified_data)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(Person.objects.get().job, "software engineer")
        self.assertEqual(Person.objects.get().email, "billysmith@test.com")   

        response = self.client.patch(self.url_person_1, self.full_modified_data)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.get().job, "Librarian")
        self.assertEqual(Person.objects.get().email, "jki@goole.com")  


    def test_delete_person(self):
        '''
        test PersonViewSets delete method
        '''
        self.assertEqual(Person.objects.count(), 0)

        PersonTestCase.test_create_person(self)
        self.assertEqual(Person.objects.count(), 1)

        response = self.client.delete(self.url_person_1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Person.objects.count(), 0)       
        