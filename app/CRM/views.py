from django.shortcuts import render, HttpResponse 
from django.contrib.auth.decorators import login_required
from .models import Stock_item as ST
from .models import Transaction as TS
# Create your views here.

def Transactions(request):
    return  render(request,'Transactions.html')

@login_required
def DB(request):
    Stok = ST.objects.filter(owner=request.user)
    Stok  = list(Stok)
    print(Stok)
    return render(request, 'DB.html', {'db':Stok})

def Stock(request):
    return render(request, 'Stock.html')

def DB_item(request):
    return render(request, 'DB_item.html')

def Stock_item(request):
    return render(request, 'Stock_item.html')



def LogIn(request):
    return render(request, 'login.html')
