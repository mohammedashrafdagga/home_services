from django.contrib import admin
from django.contrib.auth.models import User, Group
# from .models import CodeActivate


# # # Register your models here.
# # admin.site.register(CodeActivate)
admin.site.unregister(User)
admin.site.unregister(Group)


admin.site.site_header = 'Home Services'
admin.site.site_title = 'Home Services Admin Panel'
admin.site.index_title = 'Home Services'