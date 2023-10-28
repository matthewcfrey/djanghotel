from django.db import models

# Create your models here.
class Responses(models.Model):
    keyword = models.CharField(primary_key=True, max_length = 50)
    resp = models.CharField(max_length = 500)
    def __str__(self):
        return self.keyword