from django.db import models

# Create your models here.
class FeedbackModel(models.Model):
    email = models.EmailField(max_length=100)
    message = models.TextField()
