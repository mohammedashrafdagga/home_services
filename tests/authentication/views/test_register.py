import pytest
from django.test import Client
from django.contrib.auth.models import User
from apps.authentication.models import CodeActivate


from django.urls import reverse

@pytest.mark.django_db
def test_register_view():
    # Create a client for making requests
    client = Client()

    # Define the data for registration
    data = {
        'email': 'test@example.com',
        'first_name': 'John',
        'last_name': 'Doe',
        'password': 'testpassword'
    }

    # Make a POST request to the registration view
    url_path = reverse('authentication:register')
    response = client.post(url_path, data)

    # Assert that the user was registered successfully
    assert response.status_code == 201
    assert response.data['detail'] == 'الحساب ثم إنشاؤه بالفعل, قم بتفعيل الحساب'

    # Retrieve the newly created user
    user = User.objects.get(email='test@example.com')

    # Assert that the username is equal to the email
    assert user.username == 'test@example.com'

    # Assert that a CodeActivate instance was created for the user
    assert CodeActivate.objects.filter(user=user).exists()


    # Assert that registration fails with status 400 and appropriate message
    response  = client.post(url_path, data)
    assert response.status_code == 400
    assert str(response.data['detail'][0]) == "المستخدم مسجل بالفعل, قم بتسجيل الدخول"


@pytest.mark.django_db
def test_account_activation_success():
    # Create a client for making requests
    client = Client()

    # Create a user and a corresponding activation code
    user = User.objects.create(username='testuser')
    CodeActivate.objects.create(user=user, code='12345')

    # Send a POST request to the activation endpoint with the correct code
    response = client.post(reverse('authentication:verify-code'), {'code': '12345'})

    # Assert that the activation is successful
    assert response.status_code == 200
    assert response.data['detail'] == "الحساب ثم تفعيله, قم بتسحيل الدخول"

    # Refresh the user instance from the database
    user.refresh_from_db()

    # Assert that the user is now active
    assert user.is_active


@pytest.mark.django_db
def test_account_activation_failure():
    # Create a client for making requests
    client = Client()

    # Create a user and a corresponding activation code
    user = User.objects.create(username='testuser', is_active = False)
    CodeActivate.objects.create(user=user, code='12345')

    # Send a POST request to the activation endpoint with an incorrect code
    response = client.post(reverse('authentication:verify-code'), {'code': '65432'})

    # Assert that the activation fails
    assert response.status_code == 400
    assert response.data['detail'] == "الكود الذي قمت بإدخاله غير صحيح"

    # Refresh the user instance from the database
    user.refresh_from_db()

    # Assert that the user is still inactive
    assert not user.is_active

