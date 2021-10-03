from . import views

from django.conf.urls import url
from django.urls import include, path

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"items", views.ItemViewSet)
router.register(r"lists", views.ListViewSet)

urlpatterns = [
    # path("", views.HomePageView.as_view()),
    path("", include(router.urls)),
    path("signup/", views.signup),
    url(r"^(?P<path>.*)/$", views.HomePageView.as_view(), name="home"),
]
