from django.db import models
from django.contrib import admin
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

admin.site.register(User,UserAdmin)




