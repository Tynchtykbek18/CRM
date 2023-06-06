from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from crm_root.permissions import IsOwner
from .models import CustomUser, Client
from .serializers import UserSerializer, ClientSerializer


class UserView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwner, )


class ClientList(viewsets.ReadOnlyModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAdminUser, )


class ClientCreate(generics.CreateAPIView):
    serializer_class = ClientSerializer
    permission_classes = (AllowAny, )


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    authentication_classes = (JWTAuthentication, )
    serializer_class = ClientSerializer
    permission_classes = (IsOwner, )


