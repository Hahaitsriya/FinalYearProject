from django.shortcuts import render
from transformers import pipeline
from django.db.models import Q
from authentication.models import userProfile, hospital

label2id = {
    'emotional pain': 0,
    'hair falling out': 1,
    'heart hurts': 2,
    'infected wound': 3,
    'foot ache': 4,
    'shoulder pain': 5,
    'injury from sports': 6,
    'skin issue': 7,
    'stomach ache': 8,
    'knee pain': 9,
    'joint pain': 10,
    'hard to breath': 11,
    'head ache': 12,
    'body feels weak': 13,
    'feeling dizzy': 14,
    'back pain': 15,
    'open wound': 16,
    'Internal Medicine': 17,
    'blurry vision': 18,
    'acne': 19,
    'muscle pain': 20,
    'neck pain': 21,
    'cough': 22,
    'ear ache': 23,
    'feeling cold': 24,
}

hospital_mapping = {
    0: 'Psychology',
    1: 'Trichology',
    2: 'Cardiology',
    3: 'Physiology',
    4: 'Podiatry',
    5: 'Orthopedology',
    6: 'Physiology',
    7: 'Dermatology',
    8: 'Gastrology',
    9: 'Hematology',
    10: 'Rheumatology',
    11: 'Pulmonology',
    12: 'Neurology',
    13: 'Nutritionists',
    14: 'PCP',
    15: 'Orthopedology',
    16: 'Physiology',
    17: 'Physiology',
    18: 'Opthamology',
    19: 'Dermatology',
    20: 'Myology',
    21: 'PCP',
    22: 'Pulmonology',
    23: 'ENT',
    24: 'Physiology',
}

def hospital_type(query):
    # Mapping labels to hospital types
    label_to_hospital_mapping = {}
    
    for label, id_ in label2id.items():
        hospital_type = hospital_mapping.get(id_, label)
        label_to_hospital_mapping[label] = hospital_type
         
    classifier = pipeline("sentiment-analysis", model="itsriya/my_hospital_reco")
    result = classifier(query)
    final_output = result[0]['label']
    
    # Retrieve the value from label_to_hospital_mapping
    output = label_to_hospital_mapping[final_output] 
    return output

def chatbox(request):
    user_id = request.session.get('user_id')
    user_profile = userProfile.objects.get(user_id=user_id)
    
    if request.method == 'POST':
        q = request.POST.get('q')
        # Process the user input (q) and generate a response
        user_response = process_user_input(q)
        hospital_response = process_hospital_input(q)
        return render(request, 'chatbot.html', {
            'username': user_profile.username,
            'user_id': user_id,
            'status': user_profile.user_status,
            'user_response': user_response,
            'hospital_response': hospital_response
        })
    else:
        # Handle non-POST requests (e.g., GET requests)
        return render(request, 'chatbot.html', {
            'username': user_profile.username,
            'user_id': user_id,
            'status': user_profile.user_status
        })

def process_user_input(q):
    # Process the user query and map to hospital specialization
    query = hospital_type(q)
    
    # Filter user profiles based on the mapped specialization
    filtered_users = userProfile.objects.filter(user_speciality__iexact=query)
    return filtered_users

def process_hospital_input(q):
    # Process the user query and map to hospital specialization
    query = hospital_type(q)
    
    # Filter hospitals based on the mapped specialization
    filtered_hospitals = hospital.objects.filter(hospital_specialists__iexact=query)
    return filtered_hospitals
