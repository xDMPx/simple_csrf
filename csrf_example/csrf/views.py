from django.shortcuts import render, redirect 
from django.http import HttpResponseForbidden
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, TransferForm, WithdrawForm 
from django.views.decorators.csrf import csrf_exempt

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
            withdraw_form = WithdrawForm()
            transfer_form = TransferForm()
            return render(request,'csrf/index.html', {'withdraw_form': withdraw_form, 'transfer_form': transfer_form, 'account_balance': account_balance})
        else: 
            return HttpResponseForbidden()
    else:
        return redirect('/csrf/login')

@login_required(login_url='/csrf/login/')
@csrf_exempt
def transfer(request):
    global account_balance 
    if request.method == "GET":
        amount = int(request.GET.get('amount','0'))
        account_balance -= amount
        return render(request, 'csrf/transfer.html', {'withdraw': True, 'amount': amount} )
    elif request.method == "POST":
        account = request.POST.get('account',' ')
        amount = int(request.POST.get('amount','0'))
        account_balance -= amount
        return render(request, 'csrf/transfer.html', {'withdraw': False,'account': account, 'amount': amount} )
    else:
        return HttpResponseForbidden()

