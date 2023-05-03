from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.MainPage.as_view(), name="mainapp"),
    path('item//create', views.ItemCreate.as_view(), name="item_create"),
    path('item//', views.item_all, name="item_all"),
    path('item/', views.item, name="item"),
]
