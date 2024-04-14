from django.shortcuts import render
from transformers import pipeline
from django.db.models import Q
from authentication.models import userProfile,hospital

label2id = {
'emotional pain':0,
'hair falling out':1,
'heart hurts':2,
'infected wound':3,
'foot ache':4,
'shoulder pain':5,
'injury from sports':6,
'skin issue':7,
'stomach ache':8,
'knee pain':9,
'joint pain':10,
'hard to breath':11,
'head ache':12,
'body feels weak':13,
'feeling dizzy':14,
'back pain':15,
'open wound':16,
'Internal Medicine':17,
'blurry vision':18,
'acne':19,
'muscle pain':20,
'neck pain':21,
'cough':22,
'ear ache':23,
'feeling cold':24,
}


hospital_maping = {
    0:'Pschyology',
    1:'Trichology',
    2:'Cardiology',
    3:'Physiology',
    4:'Podiatry',
    5:'Orthopedology',
    6:'Physiciology',
    7:'Dermatology',
    8:'Gastrology',
    9:'Hematology',
    10 :'Rheumatology',
    11:'Pulmonology',
    12 :'Neurology',
    13 :'Nutritionists',
    14 :'PCP',
    15 :'Orthopodology',
    16 : 'Physiology',
    17 :'Physiology',
    18 : 'Opthamology',
    19 : 'Dermatology',
    20 : 'Myology',
    21 : 'PCP',
    22 : 'Pulmonology',
    23 : 'ENT',
    24 : 'Physiology',
}

def hospital_type(query):
    # Mapping labels to hospital types
    label_to_hospital_mapping = {}
    
    for label, id_ in label2id.items():
        hospital_type = hospital_maping.get(id_,label)
        label_to_hospital_mapping[label] = hospital_type         
    classifier = pipeline("sentiment-analysis", model="itsriya/my_hospital_reco")
       
    result = classifier(query)
    final_ouput = result[0]['label']
    
    # Retrieve the value from label_to_hospital_mapping
    output = label_to_hospital_mapping[final_ouput] 
    return output


# view function for the chatbox
def chatbox(request):
    user_id = request.session.get('user_id')
    user_profile = userProfile.objects.get(user_id=user_id)
    hospital = hospital.objects.get(user_id=id)

    
    if request.method == 'POST':
        q = request.POST.get('q')
        # Process the user input (q) and generate a response
        response = process_user_input(q)
        print(response)
        return render(request, 'chatbot.html',{'username':user_profile.username,'user_id':user_id,'status':user_profile.user_status,'response': response})
    else:
        # Handle non-POST requests (e.g., GET requests)
        return render(request, 'chatbot.html',{'username':user_profile.username,'user_id':user_id,'status':user_profile.user_status})


# Processing the query from the users
def process_user_input(q):
    
    query = hospital_type(q)
    print(query)
    profile = hospital.objects.filter(
        Q(hospital_specialists__exact=query)
    )
    return profile
    