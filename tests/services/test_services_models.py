import pytest
from django.contrib.auth.models import User
from apps.services.models import Category, Services, IncludeServices, NotIncludeServices

@pytest.mark.django_db
def test_category_str_representation():
    user = User.objects.create(username='testuser')
    category_name = 'Test Category'
    category = Category.objects.create(created_by=user, name=category_name)

    assert str(category) == category_name



@pytest.mark.django_db
def test_services_str_representation():
    user = User.objects.create(username='testuser')
    category = Category.objects.create(name='Test Category')
    service_name = 'Test Service'
    service = Services.objects.create(created_by=user, category=category, name=service_name)

    assert str(service) == service_name


@pytest.mark.django_db
def test_include_services_str_representation():
    user = User.objects.create(username='testuser')
    category = Category.objects.create(name='Test Category')
    services = Services.objects.create(created_by=user, category=category, name='Test Service')
    descriptions = 'This is an include service'

    include_service = IncludeServices.objects.create(services=services, descriptions=descriptions)

    assert str(include_service) == descriptions


@pytest.mark.django_db
def test_non_include_services_str_representation():
    user = User.objects.create(username='testuser')
    category = Category.objects.create(name='Test Category')
    services = Services.objects.create(created_by=user, category=category, name='Test Service')
    descriptions = 'This is a non-include service'

    non_include_service = NotIncludeServices.objects.create(services=services, descriptions=descriptions)

    assert str(non_include_service) == descriptions
