from .models import List, Item
from .serializers import ListSerializer, ItemSerializer

from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "lists/index.html", context=None)


class ListViewSet(viewsets.ModelViewSet):
    """Api endpoint to return lists in the system"""

    queryset = List.objects.all()
    serializer_class = ListSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """Api endpoint to return urls in the system"""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
