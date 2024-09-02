from django.contrib import admin
from django.urls import path
from . import views

app_name = 'million'
urlpatterns = [
    path('',views.home,name='home'),
    path('utility/',views.utility,name='utility'),
    path('<str:utility_type>/check/',views.check,name='check'),
    # path('pay_electric/',views.pay_electric,name='pay_electric'),
    # path('pay_gas/',views.pay_gas,name='pay_gas'),
    # path('pay_water/',views.pay_water,name='pay_water'),
    path('pay_all/',views.pay_all,name='pay_all'),
    path('bank/',views.bank,name='bank'),
    #path('<str:bank_type>/check_bank/',views.check_bank,name='check_bank'),
]



