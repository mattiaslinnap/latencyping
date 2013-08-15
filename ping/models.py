from django.db import models

# Create your models here.


class Upload(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    name = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
