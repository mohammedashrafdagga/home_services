import pytest
from django.test import Client
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse

@pytest.mark.django_db
def test_login_for_active_user():
    # Create a client for making requests
    client = Client()

    # Create a user and set the user as active
    user = User.objects.create(username='testuser', is_active=True)
    user.set_password('testpassword')
    user.save()

    # Send a POST request to the login endpoint with valid credentials
    response = client.post(reverse('authentication:login'),
                           {'username': 'testuser', 'password': 'testpassword'})

    # Assert that the login is successful
    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data

    # Assert that the tokens are valid
    refresh = response.data['refresh']
    
    decoded_refresh = RefreshToken(refresh)
    assert decoded_refresh['user_id'] == user.id


 


@pytest.mark.django_db
def test_login_for_not_active_user():
    # create client instance
    client = Client()
    
    # Create a user and set the user as inactive
    inactive_user = User.objects.create(username='inactiveuser', is_active=False)
    inactive_user.set_password('testpassword')
    inactive_user.save()

    # Send a POST request to the login endpoint with inactive user credentials
    response = client.post(reverse('authentication:login'),
                           {'username': inactive_user.username, 'password': 'testpassword'})
    
    assert response.status_code == 401
    assert response.data['detail'] == "No active account found with the given credentials"
