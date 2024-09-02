from django.db import models
from  django.core.validators import ValidationError
import re

# Create your models here.
def validate_kart_date(value):
    if not re.match(r'^(0[1-9]|1[0-2])\/\d{2}$', value):
        raise ValidationError(
            '%(value)s is not a valid date. Use MM/YY format.',
            params={'value': value},

        )

def validate_date(value):
    if not re.match(r'^(0[1-9]|1[0-2])\/\d{2}$', value):
        raise ValidationError(
            '%(value)s is not a valid date. Use MM/YY format.',
            params={'value': value},)

class User(models.Model):
    #onetomany relatiopnship with apartment class
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    fin_code=models.CharField(max_length=7,unique=True)#deyesen bu unique poxlari bundan basqasi istifade eliyemmez demekdi ona gore bas getsin
    personal_code=models.CharField(max_length=10, unique=True)
    birth_date = models.CharField(max_length=5, validators=[validate_date], default=None)


class Apartment(models.Model):
    address = models.CharField(max_length=255)
    unit_number = models.CharField(max_length=10)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='apartments')

class Utility(models.Model):
    apartment=models.OneToOneField(Apartment, on_delete=models.CASCADE,related_name='%(class)s_utility',default=None)
    utility_id=models.CharField(max_length=7,unique=True)
    balance=models.FloatField(default=0 )

    #bu asagidaki pox pythonda bu classin abstract class oldugunu gosterir

    class Meta:
        abstract = True

    def __str__(self):
        return f"Utility {self.utility_id} for Apartment {self.apartment.unit_number}"

    @property
    def is_balance_due(self):
        return self.balance > 0


class Utility_water(Utility):
    def __str__(self):
        return f"Water {self.utility_id} for Apartment {self.apartment.unit_number}"


class Utility_gas(Utility):
    def __str__(self):
        return f"Gas {self.utility_id} for Apartment {self.apartment.unit_number}"


class Utility_electric(Utility):
    def __str__(self):
        return f"Electric {self.utility_id} for Apartment {self.apartment.unit_number}"


#burdan sonra bank şeylərini zadı qurlaşdırmağa çalış
class Card(models.Model):
    kart_no=models.CharField(max_length=16)
    kart_date=models.CharField(max_length=5, validators=[validate_date])
    kart_cvv=models.CharField(max_length=3)
    balance=models.FloatField(default=0)

    class Meta:
        abstract=True

#bundan sonrakı bank classları bu classdan inherit eliyəcək

class Bank(Card,models.Model):
    user=models.ForeignKey(User)

    def __str__(self):
        return f"Bank {self.name} {self.surname} {self.cif_code}"


