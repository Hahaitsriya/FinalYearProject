from django.shortcuts import render,redirect
from .models import userProfile
from message.models import message

# Create your views here.
def inbox(request, user_id):
    user_id = request.session.get('user_id')
    user_profile = userProfile.objects.get(user_id=user_id)
    
    user = userProfile.objects.get(pk=user_id)
    messages = user.received_messages.all()
    return render(request, 'chat/inbox.html', {'username':user_profile.username,'user_id':user_id,'status':user_profile.user_status, 'messages': messages})

def send_message(request, sender_id, recipient_id):
    if request.method == 'POST':
        sender = userProfile.objects.get(pk=sender_id)
        recipient = userProfile.objects.get(pk=recipient_id)
        body = request.POST.get('body')
        message = message.objects.create(sender=sender, recipient=recipient, body=body)
        return redirect('inbox', user_id=recipient_id)
    return render(request, 'chat/send_message.html')

