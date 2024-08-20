from django.db import models
from django.contrib.auth.models import User

# class District(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
# class Branch(models.Model):
#     district = models.ForeignKey(District, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return f'{self.name} ({self.district.name})'

class Account(models.Model):
    ACCOUNT_TYPES_CHOICES = [
        ('savings', 'Savings'),
        ('current', 'Current'),
    ]
    MATERIALS_PROVIDED_CHOICES = [
        ('debit_card', 'Debit Card'),
        ('credit_card', 'Credit Card'),
        ('cheque_book', 'Cheque Book'),
    ]
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    # district = models.ForeignKey(District, on_delete=models.CASCADE)
    # branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES_CHOICES)
    materials_provided = models.JSONField(default=list)  # Changed to JSONField for multiple selections


    def __str__(self):
        return f'{self.name} - {self.account_type}'




