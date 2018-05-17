from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Transaction, Customer, Account


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class TransactionSerializer(serializers.ModelSerializer):

    destination_customer = serializers.CharField(source='destination_account.customer', read_only=True)
    source_customer = serializers.CharField(source='source_account.customer', read_only=True)
    source_account = serializers.CharField(read_only=True)
    destination_account = serializers.CharField(read_only=True)
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Transaction
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):

    marital_status = serializers.CharField(source='get_marital_status_display')
    gender = serializers.CharField(source='get_gender_display')

    class Meta:
        model = Customer
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):

    status = serializers.CharField(source='get_status_display')
    type = serializers.CharField(source='type.name')
    currency = serializers.CharField(source='currency.name')

    class Meta:
        model = Account
        fields = '__all__'
