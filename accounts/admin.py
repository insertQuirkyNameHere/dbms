from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model() # we could have also imported it from models.py, but this tests out that our custom model is actually being used.

class CustomUserAdmin(admin.ModelAdmin):
    search_fields = ['email'] #makes email searchable in admin site
    class Meta: #Meta class means that this ModelAdmin should actually refer to the model defined by User (as defined in line 4)
        model = User
admin.site.register(User, CustomUserAdmin) # Registers the CustomUser model to the admin so that it is displayed in the admin site
# Register your models here.
