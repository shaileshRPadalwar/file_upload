from django.db import models

# Create your models here.
class UploadFile(models.Model):
    img=models.FileField(upload_to='uploads/')
    

