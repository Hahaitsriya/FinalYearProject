from django.shortcuts import render,redirect
from appointment.models import Appointment
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Appointment
from authentication.models import userProfile
from django.utils import timezone

# Create your views here.
def user_doctor_profile(request, user_id): 
    for_nav = request.session.get('user_id') 
    profiles = userProfile.objects.get(user_id=for_nav)
    
    #for getting the profile based data.
    user_profile = get_object_or_404(userProfile, user_id=user_id)
    appointment_details = None
    
    if request.method == 'POST':
        appointment_name=request.POST.get('appointment_name')
        appointment_email=request.POST.get('appointment_email')
        appointment_time = request.POST.get('appointment_time')
        
        # Note: You'll need to adjust the format based on how the date is being sent from the frontend
        appointment_time = timezone.datetime.strptime(appointment_time, '%Y-%m-%dT%H:%M')
        
        appointment_details = Appointment.objects.create(
            appointment_name=appointment_name,
            appointment_email=appointment_email,
            appointment_time=appointment_time,
            user=userProfile.objects.get(user_id=for_nav),  # Assigning the userProfile instance
            doctor=user_profile  # Assigning the userProfile instance fetched earlier
        )
        print(appointment_details)
        # Store appointment details in session
        request.session['appointment_details'] = {
            'appointment_name': appointment_name,
            'appointment_email': appointment_email,
            'appointment_time': appointment_time.strftime('%Y-%m-%d %H:%M'),  # Convert to string for session
            
        }
       
   
    return render(request, 'profile.html',  {'username':user_profile.username,'email': user_profile.user_email,'contact': user_profile.user_contact,
                                            'status':profiles.user_status,'newStatus': user_profile.user_status,'user_profile': user_profile,
                                            'appointment_details': appointment_details})
    
    
def session(request):
    for_nav = request.session.get('user_id')
    profiles = userProfile.objects.get(user_id=for_nav)
    doctor_email=profiles.user_email
    
    # Retrieve appointment details from session
    appointment_details = request.session.get('appointment_details')
    
    if appointment_details:
        # Retrieve doctor's email from appointment details
       appointment_email = appointment_details.get('doctor_email')   
       if doctor_email:
        # Filter appointments for the specific doctor
        doctor_appointments = Appointment.objects.filter(doctor__user_email=doctor_email)
        return render(request, 'appointment/session.html', {'username':profiles.username,'email': profiles.user_email,'contact': profiles.user_contact,'status':profiles.user_status,'doctor_appointments': doctor_appointments})
    
    # Redirect to dashboard or appropriate page if appointment details are not found
    return redirect('dashboard')  


