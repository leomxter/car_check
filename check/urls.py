from django.urls import path
from check.views import home

urlpatterns= [
    path("", home ,name='index-page'),
]