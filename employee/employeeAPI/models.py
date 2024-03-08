from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="worker", null=True
    )
