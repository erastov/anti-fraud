from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status
from .serializers import UserSerializer, CurrencySerializer
import pusher
from api.models import Currency

pusher_client = pusher.Pusher(
  app_id='509691',
  key='16b0026a0399f224c710',
  secret='4b7e587592574869093d',
  cluster='eu',
  ssl=True
)


class CurrencyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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
