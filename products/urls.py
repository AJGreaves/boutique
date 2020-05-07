from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_prooducts, name='products'),
]
