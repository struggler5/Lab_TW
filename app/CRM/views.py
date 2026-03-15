from django.shortcuts import render, HttpResponse 

# Create your views here.

def Transactions(request):
    return  render(request,'Transactions.html')

def DB(request):
    return render(request, 'DB.html')

def Stock(request):
    return render(request, 'Stock.html')

def DB_item(request):
    return render(request, 'DB_item.html')

def Stock_item(request):
    return render(request, 'Stock_item.html')



def LogIn(request):
    return render(request, 'login.html')
