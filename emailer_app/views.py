from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from emailer_app.forms import FormName
from emailer.settings import EMAIL_HOST_USER
from django.core.mail import send_mail,EmailMessage
# Create your views here.

def index2(request):
    return HttpResponse("yuuuu")

def index(request):
    form=FormName()
    if request.method=="POST":
        form=FormName(request.POST,request.FILES)
        if form.is_valid():
            ls=str(form['receiver_email'].value())
            t=ls.split(',')
        #    print(t)
        #    print("name :"+form.cleaned_data['sender_name'])
        #    send_mail("subject",str(form['text'].value()),EMAIL_HOST_USER,t,fail_silently=False)
            try:
                male=EmailMessage(str(form['subject'].value()),str(form['text'].value()),EMAIL_HOST_USER,t)
                fil=request.FILES['file']
                male.attach(fil.name,fil.read(),fil.content_type)
                male.send(fail_silently=False)
                return render(request,"emailer_app/success.html")
            except:
                return render(request,"emailer_app/fail.html")
    else:
        form=FormName()
    return render(request,"emailer_app/index.html",{'form':form})
