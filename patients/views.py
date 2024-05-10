from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Patient, PastRecords
from django.contrib.auth.decorators import login_required

# Create your views here.


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        patient = Patient(username=username, name=name, password=password, email=email)
        new_user = User.objects.create_user(username=username, password=password, email=email)
        new_user.save()
        patient.save()


        print("-------------------")
        print(username, name, password, email)
        return redirect('login')

    return render(request, 'signup.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("-------------------")
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('patientHistory')
        else:
            return redirect('login')
    return render(request, 'login.html')

@login_required(login_url='login')
def patientHistory(request):
    user=request.user
    # user='test1'
    patientdetails=Patient.objects.filter(username=user)
    record=PastRecords.objects.filter(username=user)
    record_list=[i for i in record]

    print("--------------------")
    print(record_list)
    # print(patientdetails[0].username)
    print("--------------------")
    data={
        'patientName': patientdetails[0].name,
        'patientEmail': patientdetails[0].email,
        'patientUsername': patientdetails[0].username,
        'records': record_list
          }
    return render(request, 'patientHistory.html',data)

@login_required(login_url='login')
def historyReport(request):
    User=request.user
    # User='test1'
    patientdetails=Patient.objects.filter(username=User)
    print("--------------------")
    print(type(patientdetails))
    if request.method == 'GET':
        record_data=request.GET.get('report')
        record_data_req=PastRecords.objects.get(id=record_data)
        print("--------------------")
        print(type(record_data_req))
        data={
            'Name': patientdetails[0].name,
            'Email': patientdetails[0].email,
            'Date': record_data_req.date,
            'prediction': record_data_req.disease,
            'discription': record_data_req.discription,
            'medicine': record_data_req.medication,
            'precaution': record_data_req.precautions,
            'symptoms': record_data_req.symptoms,
        }
        
        return render(request, 'historyReport.html', data)
    return render(request, 'historyReport.html')