from unicodedata import name
from django.urls import path
from .views import HomePageViwe

urlpatterns = [path('', HomePageViwe.as_view(), name='home'),
]