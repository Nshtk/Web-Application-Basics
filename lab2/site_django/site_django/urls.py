from django.contrib import admin
from django.urls import path
from .views import send_json

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sendjson/', send_json, name='send_json'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
]
