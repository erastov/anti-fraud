from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, TransactionSerializer
from django.db.models.signals import post_save
from django.dispatch import receiver
from .signals import Pusher
from .models import Transaction

pusher = Pusher()


@receiver(post_save, sender=Transaction)
def service_post_save(sender, instance, **kwargs):
    serializer = TransactionSerializer(instance)
    pusher.send_message(serializer.data)


class LoginView(APIView):

    permission_classes = ()

    def post(self, request, *args, **kwargs):
        username = request.data.get('login', '')
        password = request.data.get('password', '')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(status=401)


class LogoutView(APIView):

    permission_classes = ()

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response({'logout': 'done'})

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class UserSettings(APIView):

    permission_classes = (IsAuthenticated,)
    """
    View to get current user settings
    """

    def get(self, request):
        """
        Return a user config or None.
        """
        user = request.user
        # permissions = {p.codename: True for p in Permission.objects.filter(user=user)}
        #@roles = {g.name: True for g in Group.objects.filter(user=user)}
        config = {
            'authenticated': True,
            'username': user.username,
            'roles': {'authenticated': True}
        }
        return Response(config)
