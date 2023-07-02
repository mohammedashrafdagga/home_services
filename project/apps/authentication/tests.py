from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class AuthenticationMixin():
    data = {
          
            'email': 'testuser@example.com',
            'first_name':'Mohammed',
            'last_name': 'Ashraf',
            'password': 'test_user_password'
        }
    
class RegisterUserAPITestCase(AuthenticationMixin, APITestCase):
    # test register user
    def test_register_user(self):
       
        url = reverse('authentication:register') 
        # send request to get response
        response = self.client.post(url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1) 
        self.assertEqual(User.objects.first().username, self.data['email'])
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)



class AuthenticationRegisterUserMixin(AuthenticationMixin, APITestCase):
    def setUp(self) -> None:
        # create user
        User.objects.create_user(
            username=self.data['email'],
            email=self.data['email'],
            password=self.data['password']
        )

class LoginUserAPITestCase(AuthenticationRegisterUserMixin):
    
    # login test endpoint
    def test_login_user(self):
        # 
        url = reverse('authentication:login')
        data = {
            "username": self.data['email'],
            'password': self.data['password']
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        
        
        
class ChangePasswordAPITestCase(AuthenticationRegisterUserMixin):
    def setUp(self) -> None:
        super().setUp()
        # login user
        response = self.client.post(reverse('authentication:login'), data = {
            "username": self.data['email'],
            'password': self.data['password']
        })
        self.client.credentials(HTTP_AUTHORIZATION = f"Bearer {response.data.get('access')}")
        
        
    def test_change_password(self):
        url = reverse('authentication:change-password')
        data = {
            'old_password': self.data['password'],
            'new_password1': 'test_user_password2',
            'new_password2': 'test_user_password2'
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['detail'], 'Password changed successfully')
