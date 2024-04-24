from django.shortcuts import render,redirect
from appointment.models import Appointment
from django.shortcuts import get_object_or_404, redirect
from .models import Appointment
from authentication.models import userProfile
from django.utils import timezone
from django.db.models import Q
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import JsonResponse


# Create your views here.
def search_results(request):
    for_nav = request.session.get('user_id') 
    profiles = userProfile.objects.get(user_id=for_nav)
    
    user_id = request.session.get('user_id')
    for_profile = userProfile.objects.get(user_id=user_id)
    # Retrieve the current user's profile
    user_id = request.session.get('user_id')
    current_user_profile = get_object_or_404(userProfile, user_id=user_id)
    
    # Get the search query from the request
    query = request.GET.get('q')
    
    # Perform the search if a query is provided
    if query:
        # Filter user profiles based on the search query
        object_list = userProfile.objects.filter(
            Q(username__icontains=query) |
            Q(user_email__icontains=query) |
            Q(user_speciality__icontains=query)
        )
    else:
        object_list = userProfile.objects.none()
    
    # Prepare context data to pass to the template
    context = {
        'object_list': object_list,
        'query': query,
        'current_user_profile': current_user_profile,
        'status':profiles.user_status,
        'profile_pp':for_profile.user_profile,
    }
    
    # Render the search results template with the context data
    return render(request, 'search.html',context)

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
                                            'status':profiles.user_status,'newStatus': user_profile.user_status,'user_profile': user_profile,'speciality':user_profile.user_speciality,
                                            'appointment_details': appointment_details,'profile_pp':profiles.user_profile})
    
    
def session(request):
    for_nav = request.session.get('user_id')
    profiles = userProfile.objects.get(user_id=for_nav)
    doctor_email=profiles.user_email
    
    user_id = request.session.get('user_id')
    for_profile = userProfile.objects.get(user_id=user_id)
    
    # Retrieve appointment details from session
    appointment_details = request.session.get('appointment_details')
    
    if appointment_details:
        # Retrieve doctor's email from appointment details
       appointment_email = appointment_details.get('doctor_email') 
       if doctor_email:
        # Filter appointments for the specific doctor
        doctor_appointments = Appointment.objects.filter(doctor__user_email=doctor_email)
        return render(request, 'appointment/session.html', {'username':profiles.username,'email': profiles.user_email,'contact': profiles.user_contact,'status':profiles.user_status,'doctor_appointments': doctor_appointments,'profile_pp':for_profile.user_profile})
    
    # Redirect to dashboard or appropriate page if appointment details are not found
    return redirect('dashboard')  

def accept_appointment(request):
    if request.method == 'POST':
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            appointment_id = request.POST.get('appointment_id')
            print(appointment_id)
            if appointment_id:
                appointment = Appointment.objects.get(pk=appointment_id)
                
                # Send email to the user
                user_email = appointment.appointment_email
                user_subject = "Appointment Accepted"
                user_message = render_to_string('appointment/email/user_notification.html', {'appointment': appointment})
                send_mail(user_subject, user_message, 'your_email@example.com', [user_email])
                
                # Send email to the doctor
                doctor_email = appointment.doctor.user_email
                doctor_subject = "Appointment Accepted"
                doctor_message = render_to_string('appointment/email/doctor_notification.html', {'appointment': appointment})
                send_mail(doctor_subject, doctor_message, 'your_email@example.com', [doctor_email])
                
                # Update appointment status in the database or perform any other necessary actions
                appointment.status = 'Accepted'
                appointment.save()
                
                return JsonResponse({'status': 'success'})  # Return JSON response indicating success
            else:
                return JsonResponse({'status': 'error', 'message': 'Appointment ID not provided'}, status=400)  # Return JSON response indicating error
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)  # Return JSON response indicating error
