from django.db import models

# Create your models here.
class Review(models.Model):
    name_text = models.CharField(max_length=100, blank=True)
    email_text = models.CharField(max_length=100, blank=True)
    phone_text = models.CharField(max_length=100, blank=True)
    review_text = models.CharField(max_length=100, blank=True)