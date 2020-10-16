from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField(default='Enter Descriptions:')
    isbn = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title