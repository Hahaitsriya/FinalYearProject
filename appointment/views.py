from django.shortcuts import render,redirect
from appointment.models import Appointment
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Appointment
from authentication.models import userProfile
from django.utils import timezone

# Create your views here.
def request_appointment(request):
    if request.method == 'POST':
        # Assuming the form data includes 'doctor_id' and 'appointment_time'
        doctor_id = request.POST.get('doctor_id')
        appointment_time = request.POST.get('appointment_time')
        
        # Convert the appointment_time from string to datetime object
        # Note: You'll need to adjust the format based on how the date is being sent from the frontend
        appointment_time = timezone.datetime.strptime(appointment_time, '%Y-%m-%dT%H:%M')

        
        # Ensure the user is logged in
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to request an appointment.")
            return redirect('login')
        
        # Ensure the selected doctor exists
        try:
            doctor = userProfile.objects.get(user_id=doctor_id, user_status='doctor')
        except userProfile.DoesNotExist:
            messages.error(request, "The selected doctor does not exist.")
            return render(request,'appointment/select_doctor.html')
        
        # Create the appointment
        appointment = Appointment(
            user=request.user.userprofile,  
            # Assuming you have a way to get the UserProfile from the request.user
            doctor=doctor,
            appointment_time=appointment_time,
            status='requested'
        )
        appointment.save()
        
        messages.success(request, "Your appointment request has been submitted.")
        return redirect('appointment_success')  # Redirect to a new page to show success message
    else:
        # If not a POST request, show the appointment request form
        # Assuming you have a form or a way to select a doctor and specify an appointment time
        return render(request, 'appointment/request_appointment.html')

