from django.shortcuts import render, redirect 
from django.http import HttpResponseForbidden
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, TransferForm, PayTaxesForm
from django.views.decorators.csrf import csrf_exempt

account_balance = 500
transations_history = []

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

@login_required(login_url='/csrf/login/')
def index(request):
    if request.method == 'GET':
        pay_taxes_form = PayTaxesForm()
        transfer_form = TransferForm()
        return render(request,'csrf/index.html', {'pay_taxes_form': pay_taxes_form, 'transfer_form': transfer_form, 'account_balance': account_balance, 'transations_history': transations_history})
    else: 
        return HttpResponseForbidden()

@login_required(login_url='/csrf/login/')
@csrf_exempt
def transfer(request):
    global account_balance 
    global transations_history 
    if request.method == "GET":
        amount = int(request.GET.get('amount','0'))
        account_balance -= amount
        transations_history.append(f"Tax Payment: {amount}")
        return render(request, 'csrf/transfer.html', {'tax_payment': True, 'amount': amount} )
    elif request.method == "POST":
        account = request.POST.get('account',' ')
        amount = int(request.POST.get('amount','0'))
        account_balance -= amount
        transations_history.append(f"Transfered {amount} to {account}")
        return render(request, 'csrf/transfer.html', {'tax_payment': False,'account': account, 'amount': amount} )
    else:
        return HttpResponseForbidden()

