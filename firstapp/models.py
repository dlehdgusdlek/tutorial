from django.db import models

# Create your models here.

class Curriculum(models.Model):
    name = models.CharField(max_length = 255)
    #오버라이딩: 재정의한다.
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length = 30)
    cnt = models.IntegerField()
    