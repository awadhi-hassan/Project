from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
from ComputerProject.settings import MEDIA_ROOT, BASE_DIR
from .models import Reservation, Files
from users.fingerprint import FingerPrint
import os

computer_number = 1

def encrypt(request):
    if request.POST and request.FILES:
        print(request.FILES['my_file'])
        fls = Files()
        fls.file = request.FILES['my_file']
        fls.user_id = request.user.id
        fls.save()

        filename = os.path.join(MEDIA_ROOT, 'files/' + str(request.FILES['my_file']))
        def load_key():
            return open('key', 'rb').read()
        key = load_key()
            
        def encrypt_file(filename, key):
            fernet = Fernet(key)
            with open(filename, 'rb') as f:
                data = f.read()
            enc_data = fernet.encrypt(data)
            with open(filename, 'wb') as f:
                f.write(enc_data)
        encrypt_file(filename, key)
        messsages.success(request, 'File Uploaded successfully. Remember you will have to decrypt it first if you want to view.')
        
    return render(request, template_name='encryption.html')


def decrypt(request): 
    if request.POST:
        filename = os.path.join(MEDIA_ROOT, 'files/' + request.POST['file'])
        def load_key():
            return open('key', 'rb').read()
        key = load_key()

        def decrypt_file(filename, key):
            fernet = Fernet(key)
            with open(filename, 'rb') as f:
                data = f.read()
            dec_data = fernet.decrypt(data)
            with open(filename, 'wb') as f:
                f.write(dec_data)
        decrypt_file(filename,key)
        messages.success(request, 'File decrypted successfully!')

    options = os.listdir(os.path.join(BASE_DIR, 'media/files'))
    cont = {
        'files': [file for file in options]
    }
          
    return render(request, template_name="decryption.html", context=cont)

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
        user_id = request.user.id

        rsv.computer_number = computer_number
        rsv.duration_time = int(choices['end_time']) - int(choices['start_time'])
        rsv.description = choices['description']
        rsv.user_id = user_id        
        rsv.save()
        messages.success(request, "Reservation created successfully!")

    return render(request, template_name='home.html', context={'title': 'home'})

def enroll(request):
    return render(request, template_name='enroll.html', context={'title': 'enroll'})

def fingerprint(request):
    if request.POST:
        names = request.POST
        usr = User()
        usr.first_name = names['first_name']
        usr.last_name = names['last_name']
        usr.username = names['username']
        usr.set_password(names['password'])
        usr.save()
        print(usr.last_name)

    fp = FingerPrint()
    try:
        fp.open()
        print("Please touch the fingerprint sensor")
        if fp.verify():
            return render(request, template_name='fingerprint.html')
        else:
            return render(request, template_name='fail.html')
    finally:
        fp.close()

def reserve(request):
    cont = {
        'title': 'reserve',
        'options' : [x for x in range(1,11)],
        'computer_number' : computer_number 
        }

    return render(request, template_name='reserve.html', context=cont)
