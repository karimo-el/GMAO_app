from django.contrib import admin
from .models import work_request
from django.contrib.auth.models import Group

# Register your models here. 
admin.site.register(work_request)
admin.site.unregister(Group)

