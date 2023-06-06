from rest_framework import viewsets
from .models import Deal
from .serializers import DealSerializer
from crm_root.permissions import IsOwner


class DealView(viewsets.ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    permission_classes = (IsOwner, )

