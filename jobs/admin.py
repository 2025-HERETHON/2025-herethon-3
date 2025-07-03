from django.contrib import admin
from .models import FieldCategory, InterestTag, Job

# Register your models here.

admin.site.register(Job)
admin.site.register(InterestTag)
admin.site.register(FieldCategory)

