from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name=""),
    
    path('register', views.register, name="register"),
    
    path('login', views.login, name="login"),
    
    path('dashboard', views.dashboard, name="dashboard"),
    
    path('contact', views.contact, name="contact"),
    
    path('about', views.about, name="about"),
    
    path('services', views.xray, name="X-ray"),
        
    path('symptom', views.diagnosis, name="symptomes"),
    
    path('diagnosis', views.diagnosis, name='diagnosis-result'), 
    
    path('logout', views.logout, name="logout"),
    
    
    

    
]