from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    admin_reply = models.TextField(blank=True)
