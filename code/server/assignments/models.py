from django.db import models
from django.conf import settings
from courses.models import Course

class Assignment(models.Model):
    name = models.CharField(null=False, max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assignment_type_id = models.ForeignKey('AssignmentType', on_delete=models.CASCADE)
    course_id = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    description = models.TextField()
    full_points = models.IntegerField()
    due_at = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    accepts_submissions = models.BooleanField()


class AssignmentType(models.Model):
    name = models.CharField(null=False, max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    student_weightable = models.BooleanField()
    has_max_points = models.BooleanField()
    max_points = models.IntegerField()
    attendance = models.BooleanField()
    position = models.IntegerField()
    top_grades_counted = models.IntegerField()
    course_id = models.ForeignKey('courses.Course', on_delete=models.CASCADE)

class AssignmentTypeWeight(models.Model):
    weight = models.IntegerField()
    assignment_type_id = models.ForeignKey('AssignmentType', on_delete=models.CASCADE)
    course_id = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()