from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Transaction


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class TransactionSerializer(serializers.ModelSerializer):

    source_account = serializers.CharField(read_only=True)
    destination_account = serializers.CharField(read_only=True)
    source_card = serializers.CharField(read_only=True)
    destination_card = serializers.CharField(read_only=True)
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Transaction
        fields = '__all__'
