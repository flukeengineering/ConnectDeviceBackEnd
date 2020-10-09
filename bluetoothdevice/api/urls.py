from django.urls import path
from bluetoothdevice.api.views import UserRegister,UserEdit,ConnectDeviceCreate,ConnectDeviceDetail

urlpatterns = [
    path('register/', UserRegister.as_view(), name="register"),
    path('user/<int:pk>/edit', UserEdit.as_view(), name="register-edit"),
    path('connectdevice/',ConnectDeviceCreate.as_view(), name="connectdevice"),
    path('connectdevice/<int:pk>/',ConnectDeviceDetail.as_view(), name="connectdevice-detail"),
]
