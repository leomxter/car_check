from django.urls import path
from check.views import HomePage

urlpatterns= [
    path('home/', HomePage, name='home-page'),
]