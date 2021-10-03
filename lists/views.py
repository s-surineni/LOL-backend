from django.http import HttpResponse

from .models import List, Item
from .serializers import ListSerializer, ItemSerializer

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from rest_framework import viewsets


class HomePageView(TemplateView):
    def get(self, request, path="", **kwargs):
        return render(request, "lists/index.html", context=None)


class ListViewSet(viewsets.ModelViewSet):
    """Api endpoint to return lists in the system"""

    queryset = List.objects.all()
    serializer_class = ListSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """Api endpoint to return urls in the system"""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# TODO may not be correct app for authentication?
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("home", {"path": ""})
    else:
        form = UserCreationForm()
    return HttpResponse("done")
    # return render(request, "signup.html", {"form": form})
