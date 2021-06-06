from django.shortcuts import render
from .models import UploadFile
from .forms import UploadForm
# Create your views here.



def Upload(request): 
    form=UploadForm() 
    if request.method=="POST":
        form=UploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    files=UploadFile.objects.all()
    return render(request,'testapp/home.html',{'files':files,'form':form})

