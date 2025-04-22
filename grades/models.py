from django.db import models

class Grade(models.Model):
    apogee = models.CharField(max_length=20)
    cin = models.CharField(max_length=20)
    full_name = models.CharField(max_length=100)
    module = models.CharField(max_length=100)
    grade = models.FloatField()
    result = models.CharField(max_length=20)
    session = models.CharField(max_length=50)
    year = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.full_name} - {self.module}"