from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register([Show, Season, Episode, User_show_info, Genre])