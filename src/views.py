from django.shortcuts import render, redirect
from .models import Store, Photos
from django.contrib.auth import authenticate, login
from .forms import SignInForm
from django.contrib.auth.forms import AuthenticationForm




def title(request):
    return render(request, 'templates/nones.html') 

def bo(request):
    return render(request, 'templates/types/phone1.html') 

def bo2(request):
    return render(request, 'templates/types/phone2.html') 

def bo3(request):
    return render(request, 'templates/types/phone3.html') 

def bo4(request):
    return render(request, 'templates/types/phone4.html') 

def bo5(request):
    return render(request, 'templates/types/phone5.html') 

def bo5(request):
    return render(request, 'templates/types/phone5.html') 

def bo6(request):
    return render(request, 'templates/types/phone6.html') 

def bo7(request):
    return render(request, 'templates/types/phone7.html') 

def bo8(request):
    return render(request, 'templates/types/phone8.html') 

def bo9(request):
    return render(request, 'templates/types/phone9.html') 


def signup(request):

    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('title')
          
    else:
        form = SignInForm()
    return render(request, 'templates/registrations/signup.html', {'form': form})

def user_login(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user=user)

            
                return redirect('title')
        
    else:
        form = AuthenticationForm()
    return render(request, 'templates/registrations/login.html', {'form': form})




    


