from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=40)
    code = models.IntegerField()



class Employee(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    profession = models.CharField(max_length=40)


class Homework(models.Model):
    name = models.CharField(max_length=40)
    due_date = models.DateField()
    is_delivered = models.BooleanField()
