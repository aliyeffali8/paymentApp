from django.apps import AppConfig


class MillionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'million'


# if utility_type == 'electric':
#
#     amount = request.POST['amount']
#
#     if amount.isdigit():
#         amount = float(amount)
#         try:
#
#             electric_utility = models.Utility_electric.objects.get(utility_id=utility_id)
#
#             electric_utility.balance += amount
#             electric_utility.save()
#             apartment = electric_utility.apartment
#
#             return render(request, "million/succesfully.html", {"apartment": apartment})
#
#         except models.Utility_electric.DoesNotExist:
#             return render(request, "404.html", {'message': 'Utility not found'})
#
#     else:
#         return render(request, "404.html", {"message": "Invalid amount"})