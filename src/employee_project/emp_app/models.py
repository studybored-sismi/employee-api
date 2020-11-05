from django.db import models

class Salary(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
