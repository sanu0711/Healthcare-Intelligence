from django.urls import path
from patients import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('patientHistory/', views.patientHistory, name='patientHistory'),
    path('historyReport/', views.historyReport, name='historyReport'),

    
]

