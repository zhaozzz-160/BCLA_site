from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class NetworkNode(models.Model):
    node_name = models.CharField(max_length=15)
    node_description = models.TextField()

    def __str__(self):
        return self.node_name


class NetworkEdge(models.Model):
    Source = models.TextField()
    Target = models.TextField()
    Weight = models.IntegerField()

    def __str__(self):
        return self.Source + "->" + self.Target
