from django.db import models

# Create your models here.
class UserMessage(models.Model):
    username = models.CharField(max_length = 50)
    message = models.CharField(max_length = 10000)
    def __str__(self):
        return self.username