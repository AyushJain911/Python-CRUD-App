from django.db import models

# Create your models here.
class user (models.Model):
    email = models.EmailField(max_length=20)
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=100)


def __str__(self):
        return self.username