from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, UploadImageForm
import numpy as np
import pandas as pd
import os
from .predict import predict_image 
from .predict import predict_image_tuberculosis



#to stop a user from accessing to the dashboard if he's loged out

from django.contrib.auth.decorators import login_required

#These are auth models & functions

from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate, login, logout
from .forms import Know_Disease
from .disease2 import NaiveBayes 
from .models import Finalis
from tensorflow import keras

def home(request):
    
    return render(request, 'index.html')


def register(request):
    
    form = CreateUserForm()
    
    if request.method == "POST": #if we got a post from the register.html page
        
        form = CreateUserForm(request.POST)  #then the user infos will be sent to the DB

        if form.is_valid():  #checks if the infos are valid/no error
            
            form.save()  #pushes all the data  to the DB if it's valid

            return redirect("login") #after registration, the user will be redirected to the login page
        
    context = {'registerform': form}     #this is to render the form to the register.html
    
    return render(request, 'register.html', context=context)



def login(request):
    
    form = LoginForm()
    
    if request.method == 'POST':
        
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                
                auth.login(request, user)
                
                return redirect("dashboard")
            
    context = {'loginform':form}
    
    
    return render(request, 'login.html', context=context)



def logout(request):
    
    auth.logout(request)
    
    return redirect("")




@login_required(login_url="login")
def dashboard(request):
    
    return render(request, 'index.html')


def about(request):
    
    return render(request, 'about.html')

def contact(request):
    
    return render(request, 'contact.html')

#############################################################
def xray(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()  # Save the uploaded image
            image_path = uploaded_image.image.path  # Path of the image on the filesystem
            
            # Check which button was clicked
            disease = request.POST.get('disease')
            
            if disease == 'pneumonie':
                prediction_label = predict_image(image_path, 'cnn_model.h5')  # Predict Pneumonia
            elif disease == 'tuberculosis':
                prediction_label = predict_image_tuberculosis(image_path, 'cnn_model1.h5')  # Predict Tuberculosis
            else:
                prediction_label = 'Unknown disease'
            
            return render(request, 'services/X-ray.html', {'form': form, 'prediction_label': prediction_label})
    else:
        form = UploadImageForm()
    return render(request, 'services/X-ray.html', {'form': form})


##############################################################
# def xray_pneu(request):
#     if request.method == 'POST':
#         form = UploadImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             uploaded_image = form.save()  # Sauvegarde de l'image téléchargée
#             image_path = uploaded_image.image.path  # Chemin de l'image sur le système de fichiers
#             prediction_label = predict_image(image_path, 'cnn_model.h5')  # Prédiction de la maladie
#             return render(request, 'services/X-ray.html', {'form': form, 'prediction_label': prediction_label})
#     else:
#         form = UploadImageForm()
#     return render(request, 'services/X-ray.html', {'form': form})

################################Covid Prediction############
# def xray_tub(request):
#     if request.method == 'POST':
#         form = UploadImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             uploaded_image = form.save()  # Sauvegarde de l'image téléchargée
#             image_path = uploaded_image.image.path  # Chemin de l'image sur le système de fichiers
#             prediction_label = predict_image_tuberculosis(image_path, 'cnn_model1.h5')  # Prédiction de la maladie
#             return render(request, 'services/X-ray.html', {'form': form, 'prediction_label': prediction_label})
#     else:
#         form = UploadImageForm()
#     return render(request, 'services/X-ray.html', {'form': form})

#############################################################
def diagnosis(request):
    if request.method == 'POST':
        form = Know_Disease(request.POST)
        if form.is_valid():
            form.save()
            symptoms = [
                form.cleaned_data['symptom1'],
                form.cleaned_data['symptom2'],
                form.cleaned_data['symptom3'],
                form.cleaned_data['symptom4'],
                form.cleaned_data['symptom5']
            ]
            symptoms = [symptom_instance.name for symptom_instance in symptoms]
            prediction = NaiveBayes(symptoms)
            instance = form.save()

            final = Finalis.objects.create(
                info=instance,
                diag=prediction
            )
            
            context = {'form': form, 'predicted_disease1': prediction, 'symptoms': symptoms}
            return render(request, "Services/result.html", context)
    else:
        form = Know_Disease()
        context = {'form': form}
        return render(request, "Services/symp.html", context)
   






