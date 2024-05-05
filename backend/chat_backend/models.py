from django.contrib.auth.models import User
from django.db import models

class ChatRoom(models.Model):
    name = models.CharField(max_length=255)

class Message(models.Model):
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
