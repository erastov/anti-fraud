from django.db import models
from django.core.validators import RegexValidator


class Customer(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    MARITAL_CHOICES = (
        ('M', 'Married'),
        ('S', 'Single'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
        ('C', 'Civil'),
    )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'")

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    home_phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    work_phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    mobile_phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    marital_status = models.CharField(max_length=1, choices=MARITAL_CHOICES)
    reputation_score = models.PositiveSmallIntegerField()


class AccountType(models.Model):

    name = models.CharField(max_length=100)


class Currency(models.Model):

    name = models.CharField(max_length=3)
    full_name = models.CharField(max_length=50)


class Account(models.Model):

    number = models.UUIDField()
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    type = models.ForeignKey(AccountType, on_delete=models.PROTECT)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    credit = models.BooleanField(default=False)


class Card(models.Model):

    TYPE_CHOICES = (
        ('C', 'Credit'),
        ('D', 'Debit'),
    )
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('B', 'Block'),
        ('F', 'Frozen'),
    )
    number_regex = RegexValidator(regex=r'^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})$',
                                  message="Card number must valid for Visa or Mastercard")
    number = models.CharField(validators=[number_regex], max_length=16)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    credit_limit = models.DecimalField(max_digits=6, decimal_places=2)
    used_credit_limit = models.DecimalField(max_digits=6, decimal_places=2)
    cvv = models.CharField(max_length=3)
    issue_date = models.DateTimeField()
    expiration_date = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    frozen_expiration_date = models.DateTimeField()


class Transaction(models.Model):

    number = models.UUIDField()
    source_account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='outgoing_transactions')
    destination_account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='incoming_transactions')
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    score = models.PositiveSmallIntegerField()
