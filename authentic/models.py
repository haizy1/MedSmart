from django.db import models


class Symptomis(models.Model):
    name =  models.CharField(max_length=100)
    def __str__(self):
        return self.name
        


class Diagnosis(models.Model):
    name = models.CharField('name',max_length=120) 
    cin = models.CharField('cin',max_length=15)
    symptom1 = models.ForeignKey(Symptomis, on_delete=models.SET_NULL,null=True, related_name='symtpom1')
    symptom2 = models.ForeignKey(Symptomis, on_delete=models.SET_NULL,null=True, related_name='symtpom2')
    symptom3 = models.ForeignKey(Symptomis, on_delete=models.SET_NULL,null=True, related_name='symtpom3')
    symptom4 = models.ForeignKey(Symptomis, on_delete=models.SET_NULL,null=True, related_name='symtpom4')
    symptom5 = models.ForeignKey(Symptomis, on_delete=models.SET_NULL,null=True, related_name='symtpom5')
    def __str__(self):
        return self.name
    
    
class Finalis(models.Model):
    info = models.ForeignKey(Diagnosis, on_delete=models.SET_NULL,null=True, related_name='info')
    diag = models.CharField('diag',max_length=120)

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploaded_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)