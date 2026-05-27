from django.db import models

# Create your models here.

# Create your models here.
class Student(models.Model):
    name=models.TextField(max_length=20)
    email=models.EmailField(unique=True)
    course=models.TextField(max_length=20)
    age=models.IntegerField(max_length=20)

    def __str__(self):
        return self.name