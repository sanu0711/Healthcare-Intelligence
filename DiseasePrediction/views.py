from django.http import HttpResponse
from django.shortcuts import render,redirect
import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import markdown

from AIchatBot.views import associatedDisease,AIbot
from patients.models import Patient, PastRecords
from AIchatBot.models import Disease
from AllDataHub.models import HospitalHub, DiseaseDetails

sympt=['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']
dictlist=[]
def disease_prediction(dis):
    set1=list(set(dis))
    dict1={key:dis.count(key) for key in set1}
    max1=max(dict1.values())
    for key in dict1.keys():
        if dict1[key]==max1:
            return key
    


def get_disease_data(name,disease,disList):
    symptom_Description=pd.read_csv('./dataset/symptom_Description.csv')
    symptom_precaution=pd.read_csv('./dataset/symptom_precaution.csv')
    medication=pd.read_csv('./dataset/Medication.csv')
    str_sympt=""
    for i in disList:
        str_sympt+=i+","


    dis_final=disease_prediction(disease)
    disc=symptom_Description[symptom_Description["Disease"]==dis_final]
    pre=symptom_precaution[symptom_precaution["Disease"]==dis_final]
    med=medication[medication["Disease"]==dis_final]
    precaut=str(pre["Precaution_1"].values[0])+","+str(pre["Precaution_2"].values[0])+","+str(pre["Precaution_3"].values[0])+","+str(pre["Precaution_4"].values[0])
    record=PastRecords(username=name,disease=dis_final,discription=disc["Description"].values[0],symptoms=str_sympt,precautions=precaut,medication=med['Medication'].values[0])
    record.save()
    data={
            "Name":name,
            "symptoms":str_sympt,
            "dt":disease[0],
            "rf":disease[1],
            "knn":disease[2],
            "svm":disease[3],
            "nb":disease[4],

            "prediction":dis_final,

           "discription":disc["Description"].values[0],
            "pre1":pre["Precaution_1"].values[0],
            "pre2":pre["Precaution_2"].values[0],
            "pre3":pre["Precaution_3"].values[0],
            "pre4":pre["Precaution_4"].values[0],

            "medicine":med["Medication"].values[0],

          }
    return data
def input_to_model(user_list):
    sympt=['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']
    symptoms = []
    for i in sympt:
        if i in user_list:
            symptoms.append(1)
        else:
            symptoms.append(0)
    return symptoms


def modelAlgosUse(choice_input):
    DT=joblib.load('./trained_models/DTmodel.pkl')
    RF=joblib.load('./trained_models/RFmodel.pkl')
    KNN=joblib.load('./trained_models/KNNmodel.pkl')
    SVM=joblib.load('./trained_models/SVMmodel.pkl')
    NB=joblib.load('./trained_models/NBmodel.pkl')
    DTpred=DT.predict([choice_input])
    RFpred=RF.predict([choice_input])
    KNNpred=KNN.predict([choice_input])
    SVMpred=SVM.predict([choice_input])
    NBpred=NB.predict([choice_input])
    l_pred=[DTpred[0],RFpred[0],KNNpred[0],SVMpred[0],NBpred[0]]
    return l_pred
    
def addDiseaseData(request):
    if request.method=='GET':
        symptom=request.GET.get('symptom')
        suggestion=associatedDisease(symptom)
        # suggestion= "under Construction"
        dictlist.append(symptom)
        return render(request,'index.html',{'symptoms':sympt,"user_Symptoms":dictlist,'suggestion':suggestion})



def max_matching_string(given_string, string_list):
    max_match_count = 0
    max_match_string = None
    
    for string in string_list:
        match_count = 0
        for char1, char2 in zip(given_string, string):
            if char1 == char2:
                match_count += 1
        
        if match_count > max_match_count:
            max_match_count = match_count
            max_match_string = string
    
    return max_match_string


def voiceSearch(request):
    if request.method=='GET':
        symptom = request.GET.get('voice-input')
        print("-------------------",symptom,"-------------------")
        fsym=max_matching_string(symptom,sympt)
        suggestion=associatedDisease(fsym)        
        # suggestion= "under Construction"
        dictlist.append(fsym)
        return render(request,'index.html',{'symptoms':sympt,"user_Symptoms":dictlist,'suggestion':suggestion})
    return render(request,'index.html',{'symptoms':sympt,"user_Symptoms":dictlist})


def submitAndPredict(request):
    if request.method=='POST':
        name = request.POST.get('Name')
        choice = request.POST.get('Disease')
        print("---------------")
        print(choice)
        choice_input=input_to_model(choice)
        print("------------------- Choice Input ------------------- ")
        print(choice_input)
        prediction=modelAlgosUse(choice_input)
        dict_resut=get_disease_data(name,prediction,dictlist)

        return render(request,'report.html' , dict_resut)
    return render(request, 'index.html',{'symptoms':sympt,'user_Symptoms':dictlist})

def index(request):
    record=Disease(disease="Covid-19",symptoms="Fever, Cough, Shortness of breath",treatments="Stay home, Stay safe",medications="Paracetamol",description="Coronavirus disease (COVID-19) is an infectious disease caused by the SARS-CoV-2 virus.")
    # record.save()

    global dictlist
    dictlist=[]
    sympt=['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']
    return render(request, 'index.html',{'symptoms':sympt,'user_Symptoms':dictlist})

def report(request):
    symptom_Description=pd.read_csv('./dataset/symptom_Description.csv')
    symptom_precaution=pd.read_csv('./dataset/symptom_precaution.csv')
    medication=pd.read_csv('./dataset/Medication.csv')
    symptom=pd.read_csv('./dataset/dataset.csv')
    str_sympt=""
    Diseases1=symptom_Description['Disease'].unique()
    Diseases2=symptom_precaution['Disease'].unique()
    Diseases3=medication['Disease'].unique()
    Diseases4=symptom['Disease'].unique()
    precaut=symptom_precaution[symptom_precaution['Disease']=='Fungal infection']
    final_precaution=str(precaut["Precaution_1"].values[0])+","+str(precaut["Precaution_2"].values[0])+","+str(precaut["Precaution_3"].values[0])+","+str(precaut["Precaution_4"].values[0])
    # print(final_precaution)
    print(precaut['Precaution_4'].values[0])

    # for disease in Diseases:
    #     desc=symptom_Description[symptom_Description['Disease']==disease]['Description'].values[0]
    #     symp=symptom[symptom['Disease']==disease]
    #     # final_symptoms=str(symp['Symptom_1'].values[0])+","+str(symp['Symptom_2'].values[0])+","+str(symp['Symptom_3'].values[0])+","+str(symp['Symptom_4'].values[0])
    #     precaut=symptom_precaution[symptom_precaution['Disease']==disease]
    #     print(precaut)
    #     # final_precaution=str(precaut["Precaution_1"].values[0])+","+str(precaut["Precaution_2"].values[0])+","+str(precaut["Precaution_3"].values[0])+","+str(precaut["Precaution_4"].values[0])
    #     med=medication[medication['Disease']==disease]['Medication'].values[0]
    #     print(med)
    #     print("Disease: ",disease,"\nDescription: ",desc,"\nSymptoms: ","final_symptoms","\nPrecautions: ","final_precaution","\nMedication: ","med")
    return render(request, 'report.html')
def AIchatBot(request):
    if request.method=='POST':
        qus=request.POST.get('user-input')
        response=AIbot(qus)
        dict1={'Question':qus,'Answer':response}
        return render(request, 'HealthAssistant.html',dict1)
    return render(request, 'HealthAssistant.html')
def AiLocation(request):
    if request.method=='GET':
        Disease=request.GET.get('disease')
        text=f"I want nearby Hospitals Details for {Disease} , Current Location=RGIPT Jais, Amethi,Uttar Pradesh India"
        resp=AIbot(text)
        return render(request, 'ailocationDetails.html',{'response':resp})
    return render(request, 'ailocationDetails.html')
def base(request):
    return render(request, 'base.html')
def test(request):
    return render(request, 'test.html')

def appointment(request):
    hospital=HospitalHub.objects.filter(hospital_name="Lapata  Hospital")
    data={
        "hospitalname":hospital[0].hospital_name,
        "location":hospital[0].location,
        "contact_information":hospital[0].contact_information,
        "doctors_and_specialists":hospital[0].doctors_and_specialists,
        "treatment_options":hospital[0].treatment_options,
        "facilities_and_amenities":hospital[0].facilities_and_amenities,
        "specialties":hospital[0].specialties,

    }
    print(data)
    if request.method=='POST':
        return render(request, 'appointment.html',data)
    return render(request, 'appointment.html',data)