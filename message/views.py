from django.shortcuts import render,redirect
from .models import userProfile,message

# Create your views here.
def inbox(request, user_id):
    user = userProfile.objects.get(pk=user_id)
    messages = user.received_messages.all()
    return render(request, 'chat/inbox.html', {'messages': messages})

def send_message(request, sender_id, recipient_id):
    if request.method == 'POST':
        sender = userProfile.objects.get(pk=sender_id)
        recipient = userProfile.objects.get(pk=recipient_id)
        body = request.POST.get('body')
        message = message.objects.create(sender=sender, recipient=recipient, body=body)
        return redirect('inbox', user_id=recipient_id)
    return render(request, 'chat/send_message.html')

