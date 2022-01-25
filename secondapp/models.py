from django.db import models
from django import forms
# from django.forms import forms
# Create your models here.
class Curriculum(models.Model):
    name = models.CharField(max_length = 255)


class Course(models.Model):
    name = models.CharField(max_length = 30)
    cnt = models.IntegerField()
    

    def __str__(self):
        return self.name


class ArmyShop(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    type = models.TextField()
    name = models.TextField()

    class Meta:
        db_table = 'army_shop'
        managed = False

class CourseForm(forms.ModelForm):
  class Meta:
    model = Course

    fields = ['name', 'cnt']  # id 속성은 PK 이므로 사용하지 않음

    labels = {  # 오류 메시지에 보여줄 단어
        'name': '과정명',
        'cnt': '인원수'
    }