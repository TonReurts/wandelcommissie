from django.contrib import admin
from django.db import models
from .models import Tocht, Wandelaar

# Register your models here.
admin.site.register(Tocht)
admin.site.register(Wandelaar)
