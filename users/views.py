from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account with username "{username}" successfully created!')
            return redirect('/')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})
