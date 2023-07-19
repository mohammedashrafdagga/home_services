from django.db import models
from django.contrib.auth.models import User

# Category Model
class Category(models.Model):
    created_by = models.ForeignKey(User,
                                   on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=20, unique=True)
    slug = models.CharField(max_length=20, null=True, blank=True)
    icon = models.ImageField(upload_to ='category_icons', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


    
class Services(models.Model):
    STATUS_CHOICES= (
        ('fixed', 'fixed'),
        ('custom', 'custom')
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='services', on_delete=models.SET_NULL, null=True, blank=True)

    # name with slug
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    slug = models.CharField(max_length=255, unique=True, null=True, blank=True)
    # status = models.CharField(max_length = 10,choices=STATUS_CHOICES, default='custom')
    
    # image services
    image = models.ImageField(upload_to='services_images', default='services_images/services.png', null=True, blank=True)
    
    # price
    price_from = models.PositiveIntegerField(default=50)
    price_to = models.PositiveIntegerField(default=250)
    
    # is active
    is_active = models.BooleanField(default=True)
    
    
    # date for services
    create_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    
    # default Manger
    objects = models.Manager()
    # quest = ServicesManger() # custom manger
    
    def __str__(self):
        return self.name

