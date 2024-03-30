from django.shortcuts import render
from transformers import pipeline

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
    1:'pschyology',
    2:'dermatology',
    3:'cardiology',
    4:'physiology',
    5:'dermatology',
    6:'gastrology',
    7:'orthopedology',
    8:'epidemiology',
    9:'neurology',
    10:'',
    11 :"",
    12 :"",
    13 :"",
    14 :"",
    15 :"",
    16 : "",
    17 :"",
    18 : "",
    19 : "",
    20 : "",
    21 : "",
    22 : "",
    23 : "",
    24 : "",
}

def hospital_type(query):

    # Mapping labels to hospital types
    label_to_hospital_mapping = {}

    for label, id_ in label2id.items():
        hospital_type = hospital_maping.get(id_,label)
        label_to_hospital_mapping[label] = hospital_type

    #  
    classifier = pipeline("sentiment-analysis", model="itsriya/my_hospital_reco")
    result = classifier(query)
    final_ouput = result[0]['label']

    # Retrieve the value from label_to_hospital_mapping

    output = label_to_hospital_mapping[final_ouput]
  
    return output

# Create your views here.
def message_response(request):
    
    query = "i have heart pain"
    
    hos_type = hospital_type(query)
    
    return render(request,'chatbot.html',{'hos_type':hos_type})

    