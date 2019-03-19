from django.db import models

# Create your models here.
class Assign(models.Model):
    Student = models.CharField(max_length=100, default="Mr x")
    test_name = models.CharField(max_length=100,  default="TEST X")
    status = models.CharField(max_length=100, default="Assigned")

    def __str__(self):
        return self.Student
