from django.db import models

# Create your models here.



class Test(models.Model):
    name = models.CharField(max_length=255 , verbose_name='Имя')
    surname = models.CharField(max_length=255 , verbose_name='Фамилия')
    age = models.CharField(max_length=255 , verbose_name='Возраст')
    
    def __str__(self):
        return '{} {}'.format(self.name , self.surname)
    

class TestNew(models.Model):
    name = models.CharField(max_length=255 , verbose_name='Имя')
    surname = models.CharField(max_length=255 , verbose_name='Фамилия')
    age = models.CharField(max_length=255 , verbose_name='Возраст')
    
    def __str__(self):
        return '{} {}'.format(self.name , self.surname)