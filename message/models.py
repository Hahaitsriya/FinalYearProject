from django.db import models
from authentication.models import userProfile

# Create your models here.
class message(models.Model):
    message_id=models.AutoField(primary_key=True)
    sender = models.ForeignKey(userProfile, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(userProfile, related_name='received_messages', on_delete=models.CASCADE)
    body = models.TextField(max_length=250,verbose_name='message_body')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} to {self.recipient}"