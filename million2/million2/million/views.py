from django.shortcuts import render
from . import models

# Create your views here.

def home(request):
    return render(request,"million/home.html")

def utility(request):
    return render(request,"million/utility.html")


from django.shortcuts import render
from . import models

#sikdir get djangoda session arasdir ne sikimin basidi bilmirem

#bu check funksiyasi dede bahba yolu ilə olan pay üçündü
# def check(request,utility_type):
#     if request.method == 'POST':
#
#         utility_id = request.POST['utility_id']
#
#         if utility_type == 'electric' :
#             electric_utility = models.Utility_electric.objects.get(utility_id=utility_id)
#             apartment = electric_utility.apartment
#
#             return render(request, "million/pay_electric.html", {
#                 "apartment": apartment
#             })
#
#
#
#             # return render(request, "million/pay_electric.html",
#             #               {"user": user, "utility": electric_utility, "apartment": apartment})
#
#         elif utility_type == 'gas' :
#             gas_utility = models.Utility_gas.objects.get(utility_id=utility_id)
#             apartment = gas_utility.apartment
#
#
#             return render(request, "million/pay_gas.html",
#                           {"apartment": apartment})
#
#         elif utility_type == 'water' :
#             water_utility = models.Utility_water.objects.get(utility_id=utility_id)
#             apartment = water_utility.apartment
#
#
#             return render(request, "million/pay_water.html",
#                           { "apartment": apartment})
#
#
#         else:
#             return render(request, "404.html")
#
#     return render(request, "million/check.html",{"utility_type":utility_type})

def check(request,utility_type):
    if request.method == 'POST':

        utility_id = request.POST['utility_id']

        if utility_type == 'electric' :
            utility = models.Utility_electric.objects.get(utility_id=utility_id)
            apartment = utility.apartment

            # return render(request, "million/pay_electric.html", {
            #     "apartment": apartment
            # })
            return render(request, "million/pay_all.html", {
                "apartment": apartment,
                "utility": utility,
                "type" : utility_type
            })


            # return render(request, "million/pay_electric.html",
            #               {"user": user, "utility": electric_utility, "apartment": apartment})

        elif utility_type == 'gas' :
            utility = models.Utility_gas.objects.get(utility_id=utility_id)
            apartment = utility.apartment
            utilityID = utility.utility_id

            # return render(request, "million/pay_gas.html",
            #               {"apartment": apartment})
            return render(request, "million/pay_all.html", {
                "apartment": apartment,
                "utility": utility,
                "type": utility_type
            })

        elif utility_type == 'water' :
            utility = models.Utility_water.objects.get(utility_id=utility_id)
            apartment = utility.apartment


            # return render(request, "million/pay_water.html",
            #               { "apartment": apartment})
            return render(request, "million/pay_all.html", {
                "apartment": apartment,
                "utility": utility,
                "type": utility_type

            })

        else:
            return render(request, "404.html")

    return render(request, "million/check.html",{"utility_type":utility_type})


def pay_all(request):
    if request.method == 'POST':

        utility_id = request.POST['utility_id']
        utility_type= request.POST['utility_type']
        print(utility_type)



        if utility_type == 'electric':

            amount=request.POST['amount']

            if amount.isdigit():
                amount=float(amount)
                try:

                    electric_utility = models.Utility_electric.objects.get(utility_id=utility_id)

                    electric_utility.balance +=amount
                    electric_utility.save()
                    apartment = electric_utility.apartment

                    return render(request, "million/succesfully.html", {"apartment": apartment})

                except models.Utility_electric.DoesNotExist:
                    return render(request, "404.html",{'message': 'Utility not found'})

            else:
                return render(request, "404.html", {"message": "Invalid amount"})




        elif utility_type == 'gas' :
            amount=request.POST['amount']

            if amount.isdigit():
                amount=float(amount)
                try:
                    gas_utility = models.Utility_gas.objects.get(utility_id=utility_id)
                    gas_utility.balance +=amount
                    gas_utility.save()
                    apartment = gas_utility.apartment
                    return render(request, "million/succesfully.html", {"apartment": apartment})

                except models.Utility_gas.DoesNotExist:
                    return render(request, "404.html")

            else:
                return render(request, "404.html", {"message": "Invalid amount"})

        elif utility_type == 'water' :
            amount=request.POST['amount']

            if amount.isdigit():
                amount=float(amount)
                try:
                    water_utility = models.Utility_water.objects.get(utility_id=utility_id)
                    water_utility.balance +=amount
                    water_utility.save()
                    apartment = water_utility.apartment
                    return render(request, "million/succesfully.html", {"apartment": apartment})

                except models.Utility_waterc.DoesNotExist:
                    return render(request, "404.html", {"message": "Utility not found"})

            else:
                return render(request, "404.html", {"message": "Invalid amount"})

    return render(request, "million/check.html",{"utility_type":utility_type})

# def pay_electric(request):
#     #bu yoxlama şeysində bir düzəltmə eləməyə çalışarsan
#     if request.POST:
#         electric_id=request.POST['utility_id']
#         amount = request.POST['amount']
#         if amount.isdigit():
#             amount = float(amount)
#             try:
#                 electric_utility=models.Utility_electric.objects.get(utility_id=electric_id)
#                 electric_utility.balance += amount
#                 electric_utility.save()
#                 apartment=electric_utility.apartment
#                 return render(request,"million/succesfully.html",{"apartment":apartment})
#
#             except models.Utility_electric.DoesNotExist:
#                     return render(request, "404.html")
#
#         else:
#             return render(request, "404.html", {"message": "Invalid amount"})
#
#     return render(request, "pay_all.html", {"message": "Invalid request method"})
#
#
# def pay_gas(request):
#     if request.POST:
#         electric_id=request.POST['utility_id']
#         amount=request.POST['amount']
#         if amount.isdigit():
#             amount = float(amount)
#             try:
#                 gas_utility=models.Utility_gas.objects.get(utility_id=electric_id)
#                 gas_utility.balance += amount
#                 gas_utility.save()
#                 apartment=gas_utility.apartment
#                 return render(request,"million/succesfully.html",{"apartment":apartment})
#             except models.Utility_gas.DoesNotExist:
#                 return render(request,"404.html")
#         else:
#             return render(request, "404.html", {"message": "Invalid amount"})
#     return render(request, "pay_all.html", {"message": "Invalid request method"})
# def pay_water(request):
#     if request.POST:
#         water_id=request.POST['utility_id']
#         amount=request.POST['amount']
#         if amount.isdigit():
#             amount = float(amount)
#             try:
#                 water_utility=models.Utility_water.objects.get(utility_id=water_id)
#                 water_utility.balance +=amount
#                 water_utility.save()
#                 apartment=water_utility.apartment
#                 return render(request,"million/succesfully.html",{"apartment":apartment})
#             except models.Utility_water.DoesNotExist:
#                 return render(request,"404.html")
#         else :
#             return render(request, "404.html", {"message": "Invalid amount"})
#     return render(request, "pay_water.html", {"message": "Invalid request method"})
#


def bank(request):
    return render(request, 'million/bank.html')

def check_bank(request,bank_type):
    pass
