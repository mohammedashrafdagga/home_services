import pytest
from django.test import Client
from apps.services.models import Services, Category
from django.urls import reverse

from django.utils import timezone


@pytest.mark.django_db
def test_get_all_services_with_search():
    # Create a client for making requests
    client = Client()

    # Create some services
    Services.objects.create(name='Service 1')
    Services.objects.create(name='Service 2')
    Services.objects.create(name='Another Service')

    # Send a GET request to the services endpoint with a search query
    response = client.get('/api/services/?q=Service')

    # Assert that the response is successful
    assert response.status_code == 200

    # Assert that the number of services returned is correct
    assert len(response.data) == 3

    # Assert that the correct services are returned
    service_names = [service['name'] for service in response.data]
    assert 'Service 1' in service_names
    assert 'Service 2' in service_names
    assert 'Another Service' in service_names


@pytest.mark.django_db
def test_get_all_categories():
    # Create a client for making requests
    client = Client()

    # Create some categories
    Category.objects.create(name='Category 1')
    Category.objects.create(name='Category 2')
    Category.objects.create(name='Another Category')

    # Send a GET request to the categories endpoint
    response = client.get(reverse('services:category-list'))

    # Assert that the response is successful
    assert response.status_code == 200

    # Assert that the number of categories returned is correct
    assert len(response.data) == 3

    # Assert that the correct categories are returned
    category_names = [category['name'] for category in response.data]
    assert 'Category 1' in category_names
    assert 'Category 2' in category_names
    assert 'Another Category' in category_names


@pytest.mark.django_db
def test_latest_add_services():
    # Create a client for making requests
    client = Client()


    for i in range(10):
        Services.objects.create(name=f'Service {i}')

    # Send a GET request to the latest-add endpoint
    response = client.get(reverse('services:latest-add'))

    # Assert that the response is successful
    assert response.status_code == 200

    # Assert that the number of services returned is correct
    assert len(response.data) == 10

    # Assert that the services are returned in the correct order (most recent first)
    # service_names = [service['name'] for service in response.data]
    # expected_names = [f'Service {i}' for i in range(9, -1, -1)]
    # assert service_names == expected_names

@pytest.mark.django_db
def test_get_services_by_category():
    # Create a client for making requests
    client = Client()

    # Create a category
    category = Category.objects.create(name='Test Category')

    # Create some services related to the category
    Services.objects.create(category=category, name='Service 1')
    Services.objects.create(category=category, name='Service 2')

    # Send a GET request to the category services endpoint
    response = client.get(reverse('services:category-detail', kwargs={'id':category.id}))

    # Assert that the response is successful
    assert response.status_code == 200

    # Assert that the number of services returned is correct
    assert len(response.data['detail']['services']) == 2

    # Assert that the correct services are returned
    service_names = [service['name'] for service in response.data['detail']['services']]
    assert 'Service 1' in service_names
    assert 'Service 2' in service_names


@pytest.mark.django_db
def test_get_service_detail():
    # Create a client for making requests
    client = Client()

    # Create a service
    service = Services.objects.create(name='Test Service')

    # Send a GET request to the service detail endpoint
    response = client.get(reverse('services:detail', kwargs={'id': service.id}))

    # Assert that the response is successful
    assert response.status_code == 200

    # Assert that the correct service data is returned
    assert response.data['name'] == 'Test Service'
