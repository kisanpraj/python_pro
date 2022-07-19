from email import message

from os import name
from django.shortcuts import render
from . views import *
from .models import *

# Create your views here.
def index(request):
    return render(request, "index.html")

#def contact(request):
    if request.method =="POST":
        try:
            if request.POST["name"] == "" or request.POST["email"] == "" or request.POST["subject"] == "" or request.POST["message"] == "":
                context = {
                "msg_d" : "All fields are mandatory..."
            }
                return render(request, "contact.html", context=context)    
            else:
                contact = contact.objects.create(
                    name = request.POST["name"],
                    email = request.POST["email"],
                    subject = request.POST["subject"],
                    message = request.POST["message"],
                ) 
                contact.save()
                subject = 'Message Sent status : SUCCESSFUL'
                message = f'Hi {contact.name}, Thank you for contacting us.\n\nOur team will get back to you within 24 hours.\n\nBest Regards....'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [contact.email, ]
                send_mail( subject, message, email_from, recipient_list )

                subject = f'Contact Request sent by {contact.name} | {contact.subject}'
                message = f"MESSAGE : \n{contact.message}"
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [settings.EMAIL_HOST_USER, ]
                send_mail( subject, message, email_from, recipient_list )

                context = {
                    "msg_s" : "Contact request sent successfully..."
                }
                return render(request, "contact.html", context=context)
        except Exception as e:
            print(f"\n\n\n{e}\n\n\n")
            context = {
                "msg_d" : "Something went wrong..."
            }
            return render(request, "contact.html", context=context)
    else:
        return render(request, "contact.html")

def contact(request):
    #data come form html to view
    
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']
    
    #creating obj of model class
    #inserting data into tabel
    newuser = contact.objects.create(name=name , email=email , subject=subject , message=message)

    #after insert renderr
    return render(request, "show.html")