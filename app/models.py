from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Disease(models.Model):
    name = models.CharField(max_length=255, null=True)
    desc = models.TextField(blank=True)
    identified_by = models.CharField(max_length=255, null=True)
    identified_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=255, null=True)
    desc = models.TextField(blank=True)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, null=True, blank=True)


