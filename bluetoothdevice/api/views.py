from django.contrib.auth.models import User
from bluetoothdevice.api.serializers import UserCreateSerializer, ConnectDeviceSerializer
from rest_framework import generics
from bluetoothdevice.models import ConnectDevice

class UserRegister(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class UserEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class ConnectDeviceCreate(generics.ListCreateAPIView):
    queryset = ConnectDevice.objects.all()
    serializer_class = ConnectDeviceSerializer

class ConnectDeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConnectDevice.objects.all()
    serializer_class = ConnectDeviceSerializer