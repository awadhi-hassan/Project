from django.shortcuts import render, HttpResponse
from .models import Fingerprint, Reservation
from django.contrib.auth.models import User
from users.fingerprint import FingerPrint

computer_number = 1

def encrypt(request):
    return render(request, template_name='encryption.html')

def decrypt(request):
    return render(request, template_name="decryption.html")

def reservation(request):
    cont={
        'title': 'reservation',
        'start_time':[start for start in range(8, 19)],
        'end_time':[end for end in range(9, 19)],
        }
    global computer_number
    computer_number=request.POST['computer_node']
    
    return render(request, template_name='reservation.html', context=cont)

def home(request):  
    rsv = Reservation()
    if request.POST:
        choices = request.POST

        rsv.computer_number = computer_number
        rsv.duration_time = int(choices['end_time']) - int(choices['start_time'])
        rsv.descriprion = choices['description']
        rsv.user = User()
        
        #rsv.save()

    return render(request, template_name='home.html', context={'title': 'home'})

def enroll(request):      
    return render(request, template_name='enroll.html', context={'title': 'enroll'})

def reserve(request):
    cont = {
        'title': 'reserve',
        'options' : [x for x in range(1,11)]
        }

    return render(request, template_name='reserve.html', context=cont)
