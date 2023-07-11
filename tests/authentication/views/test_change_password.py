import pytest
from django.test import Client
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken
from django.urls import reverse

@pytest.mark.django_db
def test_change_password_success():
    # Create a client for making requests
    client = Client()

    # Create a user
    user = User.objects.create_user(username='testuser', password='oldpassword')

    # Generate an access token for the user
    access_token = AccessToken.for_user(user)

    # Set the new password
    new_password = 'newpassword'

    # Set the request headers with the access token
    headers = {
        'HTTP_AUTHORIZATION': f'Bearer {access_token}',
    }

    # Send a POST request to the change password endpoint
    response = client.post(reverse('authentication:change-password'), {'old_password': 'oldpassword', 'new_password1': new_password, 'new_password2': new_password}, **headers)

    # Assert that the password change is successful
    assert response.status_code == 200
    assert response.data['detail'] == "ثم تغيير كلمة المرور بنجاح"

    # Refresh the user instance from the database
    user.refresh_from_db()

    # Check if the new password is set for the user
    assert user.check_password(new_password)


@pytest.mark.django_db
def test_change_password_incorrect_old_password():
    # Create a client for making requests
    client = Client()

    # Create a user
    user = User.objects.create_user(username='testuser', password='oldpassword')

    # Generate an access token for the user
    access_token = AccessToken.for_user(user)

    # Set the new password
    new_password = 'newpassword'

    # Set the request headers with the access token
    headers = {
        'HTTP_AUTHORIZATION': f'Bearer {access_token}',
    }

    # Send a POST request to the change password endpoint with incorrect old password
    response = client.post(reverse('authentication:change-password'), {'old_password': 'wrongpassword', 'new_password1': new_password, 'new_password2': new_password}, **headers)

    # Assert that the password change fails due to incorrect old password
    assert response.status_code == 400
    assert str(response.data['old_password'][0]) == "خطا في إدخال كلمة المرور"


@pytest.mark.django_db
def test_change_password_mismatched_new_passwords():
    # Create a client for making requests
    client = Client()

    # Create a user
    user = User.objects.create_user(username='testuser', password='oldpassword')

    # Generate an access token for the user
    access_token = AccessToken.for_user(user)

    # Set the request headers with the access token
    headers = {
        'HTTP_AUTHORIZATION': f'Bearer {access_token}',
    }

    # Send a POST request to the change password endpoint with mismatched new passwords
    response = client.post(reverse('authentication:change-password'), {'old_password': 'oldpassword', 'new_password1': 'newpassword1', 'new_password2': 'newpassword2'}, **headers)

    # Assert that the password change fails due to mismatched new passwords
    assert response.status_code == 400
    assert str(response.data['detail'][0]) == "تاكيد كلمة المرور لا تتشابه مع كلمة المرور الجديدة"
