from django.db import models
from django.conf import settings

class ChatRoom(models.Model):
    name = models.CharField(max_length=100)
    # Add more fields as needed

class Message(models.Model):
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    # Add more fields as needed
