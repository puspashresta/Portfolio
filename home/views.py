from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    fedback={}
    fedback['comment']=Reviews.objects.all()

    return render(request,'index.html',fedback)

def about(request):
    return render(request,'about.html')

def portfolio(request):
    return render(request,'portfolio.html')

def contact(request):
    views={}
    views['information']=Information.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']

        info= Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        info.save()
    return render(request,'contact.html',views)

def service(request):
    report={}
    report['infos']=Feedbacks.objects.all()

    return render(request,'services.html',report)

def price(request):
    return render(request,'price.html')

def bloghome(request):
    return render(request, "blog-home.html")