from .models import List, Item
from .serializers import ListSerializer, ItemSerializer
from rest_framework import viewsets

# Create your views here.


class ListViewSet(viewsets.ModelViewSet):
    """Api endpoint to return lists in the system"""

    queryset = List.objects.all()
    serializer_class = ListSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """Api endpoint to return urls in the system"""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
