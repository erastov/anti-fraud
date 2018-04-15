from django.contrib import admin
from api.models import Customer, AccountType, Currency, Account, Card, Transaction


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['number', 'customer']


@admin.register(AccountType)
class AccountTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['number', 'account', 'expiration_date']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['number', 'source_account', 'destination_account', 'score']
