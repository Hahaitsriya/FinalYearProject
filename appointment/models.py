from django.db import models
from django.utils import timezone
from authentication.models import userProfile

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('requested', 'Requested'),
        ('accepted', 'Accepted'),
        ('expired', 'Expired'),
    )
    appointment_name=models.CharField(max_length=20,verbose_name='name',blank=True, null=False)
    appointment_email=models.EmailField(max_length=200, verbose_name="User Email", blank=True, null=False)
    user = models.ForeignKey(userProfile, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(userProfile, on_delete=models.CASCADE, related_name='doctor_appointments')
    appointment_time = models.DateTimeField()
    appointment_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='requested')
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return self.appointment_status == 'requested' and timezone.now() > self.created_at + timezone.timedelta(hours=24)

