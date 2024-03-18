from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


money = 500

def index(request):
    if request.user.username != '':
        return HttpResponse(f"Hello, world to {request.user.username}. Money: {money}")
    else:
        return redirect('/csrf/login')
    

def sign_in(request):

    if request.method == 'GET':
        form = LoginForm()
        return render(request,'csrf/login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                return redirect('/csrf/')
        
        return render(request,'csrf/login.html',{'form': form})

@login_required(login_url='/csrf/login/')
def transfer(request): 
    amount = int(request.GET.get('amount','0'))
    print(f"transfering: {{amount}}")
    if request.user.username != '':
        global money 
        money -= amount
        return HttpResponse(f"{request.user.username}")
    else:
        return HttpResponse("")
        

