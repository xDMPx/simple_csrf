from django.shortcuts import render, redirect 
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, WithdrawForm 

account_balance = 500

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
    else:
        return HttpResponseForbidden()

def index(request):
    if request.user.username != '':
        if request.method == 'GET':
            form = WithdrawForm()
            return render(request,'csrf/index.html', {'withdraw_form': form, 'account_balance': account_balance})
        else: 
            return HttpResponseForbidden()
    else:
        return redirect('/csrf/login')

@login_required(login_url='/csrf/login/')
def transfer(request):
    global account_balance 
    if request.method == "GET":
        amount = int(request.GET.get('amount','0'))
        account_balance -= amount
        return render(request, 'csrf/transfer.html', {'amount': amount} )
    else:
        return HttpResponseForbidden()

