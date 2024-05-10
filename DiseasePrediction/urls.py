"""
URL configuration for DiseasePrediction project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, auth
from django.urls import path, include
from DiseasePrediction import views
from AllDataHub import viewsdata


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('report/', views.report, name='report'),
    path('addDiseaseData/', views.addDiseaseData, name='addDiseaseData'),
    path('voiceSearch/', views.voiceSearch, name='voiceSearch'),
    path('AIchatBot/', views.AIchatBot, name='AIchatBot'),
    path('', include('patients.urls')),
    path('base/', views.base, name='base'),
    path('submitAndPredict/', views.submitAndPredict, name='submitAndPredict'),
    path('import_hospitals_from_csv/', viewsdata.import_hospitals_from_csv, name='import_hospitals_from_csv'),
    path('test/', views.test, name='test'),
    path('AiLocation/', views.AiLocation, name='AiLocation'),
    path("appointment/", views.appointment, name="appointment"),
    
]
