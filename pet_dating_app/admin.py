from django.contrib import admin
from .models import PetProfile

# Register your models here.
class PetProfile(admin.ModelAdmin):
    list_display = ()