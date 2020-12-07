from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory, APIClient
from rest_framework.test import force_authenticate

from accounts.models import User
from accounts.views import AuthInfoGetView


class TestAPIViews(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = User.objects.create_user('testuser', email='testuser@test.com', password='testing')
        self.user.save()

    def test_ListAccounts_not_authenticated(self):
        request = self.factory.get('/api/users/')
        view = AuthInfoGetView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 401,
            'Expected Response Code 401, received {0} instead.'.format(response.status_code))

    def test_ListAccounts_authenticated(self):
        #self.client.login(username='testuser', password='testing') # returns True
        request = self.factory.get('/api/users/')
        force_authenticate(request, user=self.user)
        view = AuthInfoGetView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200,
            'Expected Response Code 200, received {0} instead.'.format(response.status_code))

"""
from django.test import TestCase, Client
from accounts.models import User

from rest_framework.authtoken.models import Token 
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory, APIClient

#from api.core import models, admin 
from accounts.views import AuthInfoGetView
from accounts import admin



class TestUserAccount(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            username='testuser', 
            nickname='testuser', 
            password='testing'
        )
        self.client.force_authenticate(self.user)

    def test_ListAccounts_authenticated(self): 
     self.client.login(username='testuser', password='testing') 
     #print(self.user.is_authenticated()) # returns True 
     request = self.client.get('/api/users/') 
     view = AuthInfoGetView.as_view(request, {'get':'get'}) 
     response = view(request) 
     self.assertEqual(response.status_code, 200, 
      'Expected Response Code 200, received {0} instead.'.format(response.status_code)) 

    def test_ListAccounts_not_authenticated(self): 
        request = '/api/users/'
        view = AuthInfoGetView.as_view({'get':'get'})
        response = view(request)
        self.assertEqual(response.status_code, 401, 
        'Expected Response Code 401, received {0} instead.'.format(response.status_code)) 

    def test_ListAccounts_authenticated(self): 
     self.client.login(username='testuser', password='testing') 
     print(self.user.is_authenticated()) # returns True 
     request = self.client.get('/users/') 
     view = UserViewSet.as_view({'get': 'list'}) 
     response = view(request) 
     self.assertEqual(response.status_code, 200, 
      'Expected Response Code 200, received {0} instead.'.format(response.status_code)) 
"""