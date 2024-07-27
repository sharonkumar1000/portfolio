from django.shortcuts import render
from resume.models import Contact

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        print(name,email,message)
        ins = Contact(name=name, email = email,message=message)
        ins.save()
        print("data has been written to db successfully")

    return render(request,'home.html')
