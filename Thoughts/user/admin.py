from django.contrib import admin
from .models import User, Profile

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name','username', 'email', 'is_active']



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','bio', 'address', 'img']