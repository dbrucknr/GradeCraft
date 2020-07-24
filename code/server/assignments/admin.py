from django.contrib import admin
from .models import Assignment, AssignmentType, AssignmentTypeWeight

admin.site.register(Assignment)
admin.site.register(AssignmentType)
admin.site.register(AssignmentTypeWeight)
