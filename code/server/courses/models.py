from django.db import models

class Course(models.Model):
    SEMESTERS = (
        ('FALL', 'FALL'), 
        ('WINTER', 'WINTER'), 
        ('SPRING', 'SPRING'), 
        ('SUMMER', 'SUMMER')
    )

    name = models.CharField(null=False, max_length=255)
    course_number = models.IntegerField()
    year = models.IntegerField()
    semester = models.CharField(choices=SEMESTERS, null=False, max_length=6)