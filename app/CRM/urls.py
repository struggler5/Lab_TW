from django.urls import path 
from . import views 

urlpatterns = [
        path("",views.Transactions,name="Transactions"),
        path("DB/",views.DB,name="DB"),
        path("DB_item/",views.DB_item,name="DB_item"),
        path("Stock/",views.Stock,name="Stock"),
        path("Stock_item/",views.Stock_item,name="Stock_item"),
        path("LogIn/",views.LogIn,name="LogIn")
        ]
