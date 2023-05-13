from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from mainapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mainapp/', include('mainapp.urls')),
    path('catalogue/', views.catalogue),
    path('categories/', views.categories),
    path('profile/', views.profile),
    path('health/', views.health),
    path('headquarters/', views.HeadquarterListApiView.as_view()),
    path('headquarters/<int:obj_id>/', views.HeadquarterDetailApiView.as_view()),
    path('manufacturers/', views.ManufacturerListApiView.as_view()),
    path('manufacturers/<int:obj_id>/', views.ManufacturerDetailApiView.as_view()),
    path('furniture-types/', views.FurnitureTypeListApiView.as_view()),
    path('furniture-types/<int:obj_id>/', views.FurnitureTypeDetailApiView.as_view()),
    path('products/', views.ProductListApiView.as_view()),
    path('products/<int:obj_id>/', views.ProductDetailApiView.as_view()),
    path('product-instances/', views.ProductInstanceListApiView.as_view()),
    path('product-instances/<int:obj_id>/', views.ProductInstanceDetailApiView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
