from django.contrib import admin
import uuid
from .models import Category, Services

class CategoryAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        slug = str(obj.name).replace(' ', '-')
        obj.slug = f'قسم-{slug}'
        super().save_model(request, obj, form, change)


# register into admin
admin.site.register(Category, CategoryAdmin)


# Services Admin
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id','category','name', 'slug']

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.slug = f"{str(self.validated_data['name']).replace(' ', '-')}-{uuid.uuid4()}"
        super().save_model(request, obj, form, change)


# register into admin
admin.site.register(Services, ServicesAdmin)

