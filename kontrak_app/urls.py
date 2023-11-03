from django.urls import path
from . import views

urlpatterns = [
    path('', views.kontrak, name='kontrak')
]