from django.contrib import admin
from .models import Review


# register review model to admin
admin.site.register(Review)