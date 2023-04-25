from django.urls import path
from . import views

urlpatterns = [
    path('catalogue/item/', views.item),
]