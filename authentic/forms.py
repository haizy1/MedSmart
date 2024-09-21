from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Diagnosis
from .models import UploadedImage
#This form is for registrating/creating a user(Model Form)

class CreateUserForm(UserCreationForm): 
    
    class Meta:
        
        model = User
        fields = ['username', 'email', 'password1', 'password2'] #two passwords because the user will have to re-enter the pass for verification
        
        
#This form is for authentication a user(Model Form)

class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    


#Symptoms form:
class Know_Disease(forms.ModelForm):
    class Meta:
        model = Diagnosis
        fields = ('name','cin','symptom1','symptom2','symptom3','symptom4','symptom5')

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image'] 