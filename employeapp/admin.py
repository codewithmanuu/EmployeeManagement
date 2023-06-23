from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(adminmodel)
admin.site.register(EmployeeModel)
admin.site.register(Designation)
admin.site.register(Team)
admin.site.register(leavetype)
admin.site.register(leave)