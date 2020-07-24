from django.db import models
from django.conf import settings

class Assignment(models.Model):
    name = models.CharField(null=False, max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    description = models.TextField()
    full_points = models.IntegerField()
    due_at = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    accepts_submissions = models.BooleanField()


class Assignment_Type(models.Model):
    name = models.CharField(null=False, max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    student_weightable = models.BooleanField()
    attendance = models.BooleanField()