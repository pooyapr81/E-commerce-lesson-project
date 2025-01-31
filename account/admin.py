from django.contrib import admin
from .models import Profile, Usertype
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class Profileadmin(admin.ModelAdmin):
    list_display = ('user', 'utype')


admin.site.register(Profile, Profileadmin)
admin.site.register(Usertype)
