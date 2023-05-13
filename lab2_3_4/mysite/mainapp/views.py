from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from mainapp import models
from rest_framework import status
from rest_framework.views import APIView
from mainapp import serializer
from django.db import connection
from django.db.models import Q
from django.views.generic import TemplateView
from django.core import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class MainPage(TemplateView):
    template_name = 'index.html'


def health(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return JsonResponse({"message": "OK"}, status=200)
    except Exception as ex:
        return JsonResponse({"error": str(ex)}, status=500)


@require_http_methods(["GET", "POST"])
def catalogue(request):
    if request.method == 'GET':
        return JsonResponse({"sample": "1", "sample2": 2})


@require_http_methods(["GET", "POST"])
def categories(request):
    return JsonResponse({"sample": "1", "sample2": 2})


@require_http_methods(["GET", "POST"])
def profile(request):
    return JsonResponse({"sample": "1", "sample2": 2})


@require_http_methods(["GET"])
def item(request):
    query = request.GET.get("q")
    object_list = models.Product.objects.filter(Q(name__icontains=query))
    return JsonResponse(serializers.serialize('json', object_list), safe=False)


@require_http_methods(["GET"])
def item_all(request):
    if request.method == 'GET':
        object_list = models.Product.objects.all()
        return JsonResponse(serializers.serialize('json', object_list), safe=False)


class ItemCreate(TemplateView):
    template_name = 'create.html'

    def get_context_data(self, **kwargs):
        kwargs = super(ItemCreate, self).get_context_data(**kwargs)
        kwargs['foo'] = "bar"
        return kwargs

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            action = request.POST.get("but")
            if action == "Create":
                product = models.Product.objects.create(name="Giga bed", description="That's a bed",
                                                        manufacturer=models.Manufacturer.objects.get(
                                                            name="Orange brothers factory"), price=500,
                                                        image=None)
                product.furniture_type.set(models.FurnitureType.objects.filter(name="Chair"))
                return JsonResponse(serializers.serialize(product), safe=False)


# {
#     "name": "brother",
#     "phone": "+43232"
# }

class HeadquarterListApiView(APIView):
    def get(self, request, *args, **kwargs):
        objects = models.Headquarter.objects.all()
        ser = serializer.HeadquarterSerializer(objects, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            "name": request.data.get('name'),
            "status": request.data.get('status'),
            "country": request.data.get('country'),
            "address": request.data.get('address'),
            "phone": request.data.get('phone'),
            "email": request.data.get('email'),
        }
        ser = serializer.HeadquarterSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class HeadquarterDetailApiView(APIView):
    def find(self, obj_id):
        try:
            return models.Headquarter.objects.get(id=obj_id)
        except models.Headquarter.DoesNotExist:
            return None

    def get(self, request, obj_id, *args, **kwargs):
        instance = self.find(obj_id)
        if not instance:
            return Response({"res": "Object does not exists"}, status=status.HTTP_400_BAD_REQUEST)

        ser = serializer.HeadquarterSerializer(instance)
        return Response(ser.data, status=status.HTTP_200_OK)

    def put(self, request, obj_id, *args, **kwargs):
        instance = self.find(obj_id)
        if not instance:
            return Response({"res": "Object does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        data = {
            'name': request.data.get('name'),
            'phone': request.data.get('phone'),
        }
        ser = serializer.HeadquarterSerializer(instance=instance, data=data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, obj_id, *args, **kwargs):
        instance = self.find(obj_id)
        if not instance:
            return Response({"res": "Object does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        instance.delete()
        return Response({"res": "Object deleted"}, status=status.HTTP_200_OK)

class ManufacturerListApiView(APIView):
    def get(self, request, *args, **kwargs):
        objects = models.Manufacturer.objects.all()
        ser = serializer.ManufacturerSerializer(objects, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            "headquarter": request.data.get('headquarter'),
            "name": request.data.get('name'),
            "description": request.data.get('description'),
        }
        ser = serializer.ManufacturerSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class ManufacturerDetailApiView(APIView):
    def find(self, obj_id):
        try:
            return models.Manufacturer.objects.get(id=obj_id)
        except models.Manufacturer.DoesNotExist:
            return None

    def get(self, request, obj_id, *args, **kwargs):
        instance = self.find(obj_id)
        if not instance:
            return Response({"res": "Object does not exists"}, status=status.HTTP_400_BAD_REQUEST)

        ser = serializer.ManufacturerSerializer(instance)
        return Response(ser.data, status=status.HTTP_200_OK)

    def put(self, request, obj_id, *args, **kwargs):
        instance = self.find(obj_id)
        if not instance:
            return Response({"res": "Object does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        data = {
            'name': request.data.get('name'),
            'phone': request.data.get('phone'),
        }
        ser = serializer.ManufacturerSerializer(instance=instance, data=data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, obj_id, *args, **kwargs):
        instance = self.find(obj_id)
        if not instance:
            return Response({"res": "Object does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        instance.delete()
        return Response({"res": "Object deleted"}, status=status.HTTP_200_OK)

class FurnitureTypeListApiView(APIView):
    def get(self, request, *args, **kwargs):
        objects = models.FurnitureType.objects.all()
        ser = serializer.FurnitureTypeSerializer(objects, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            "name": request.data.get('name'),
        }
        ser = serializer.FurnitureTypeSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class FurnitureTypeDetailApiView(APIView):
    def find(self, obj_id):
        try:
            return models.FurnitureType.objects.get(id=obj_id)
        except models.FurnitureType.DoesNotExist:
            return None

    def get(self, request, obj_id, *args, **kwargs):
        instance = self.find(obj_id)
        if not instance:
            return Response({"res": "Object does not exists"}, status=status.HTTP_400_BAD_REQUEST)

        ser = serializer.FurnitureTypeSerializer(instance)
        return Response(ser.data, status=status.HTTP_200_OK)

    def put(self, request, obj_id, *args, **kwargs):
        instance = self.find(obj_id)
        if not instance:
            return Response({"res": "Object does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        data = {
            'name': request.data.get('name'),
        }
        ser = serializer.FurnitureTypeSerializer(instance=instance, data=data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, obj_id, *args, **kwargs):
        instance = self.find(obj_id)
        if not instance:
            return Response({"res": "Object does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        instance.delete()
        return Response({"res": "Object deleted"}, status=status.HTTP_200_OK)

class ProductListApiView(APIView):
    def get(self, request, *args, **kwargs):
        objects = models.Product.objects.all()
        ser = serializer.ProductSerializer(objects, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            "name": request.data.get('name'),
            "description": request.data.get('description'),
            "furniture-type": request.data.get('furniture-type'),
            "manufacturer": request.data.get('manufacturer'),
            "price": request.data.get('price'),
        }
        ser = serializer.ProductSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailApiView(APIView):
    def find(self, obj_id):
        try:
            return models.Product.objects.get(id=obj_id)
        except models.Product.DoesNotExist:
            return None

    def get(self, request, obj_id, *args, **kwargs):
        instance = self.find(obj_id)
        if not instance:
            return Response({"res": "Object does not exists"}, status=status.HTTP_400_BAD_REQUEST)

        ser = serializer.ProductSerializer(instance)
        return Response(ser.data, status=status.HTTP_200_OK)

    def put(self, request, obj_id, *args, **kwargs):
        instance = self.find(obj_id)
        if not instance:
            return Response({"res": "Object does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            "furniture-type": request.data.get('furniture-type'),
        }
        ser = serializer.ProductSerializer(instance=instance, data=data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, obj_id, *args, **kwargs):
        instance = self.find(obj_id)
        if not instance:
            return Response({"res": "Object does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        instance.delete()
        return Response({"res": "Object deleted"}, status=status.HTTP_200_OK)

class ProductInstanceListApiView(APIView):
    def get(self, request, *args, **kwargs):
        objects = models.ProductInstance.objects.all()
        ser = serializer.ProductInstanceSerializer(objects, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            "id": request.data.get('id'),
            "product": request.data.get('product'),
            "status": request.data.get('status'),
            "buyer": request.data.get('buyer'),
        }
        ser = serializer.ProductInstanceSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductInstanceDetailApiView(APIView):
    def find(self, obj_id):
        try:
            return models.ProductInstance.objects.get(id=obj_id)
        except models.ProductInstance.DoesNotExist:
            return None

    def get(self, request, obj_id, *args, **kwargs):
        instance = self.find(obj_id)
        if not instance:
            return Response({"res": "Object does not exists"}, status=status.HTTP_400_BAD_REQUEST)

        ser = serializer.ProductInstanceSerializer(instance)
        return Response(ser.data, status=status.HTTP_200_OK)

    def put(self, request, obj_id, *args, **kwargs):
        instance = self.find(obj_id)
        if not instance:
            return Response({"res": "Object does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        data = {
            "status": request.data.get('status'),
            "buyer": request.data.get('buyer'),
        }
        ser = serializer.ProductInstanceSerializer(instance=instance, data=data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, obj_id, *args, **kwargs):
        instance = self.find(obj_id)
        if not instance:
            return Response({"res": "Object does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        instance.delete()
        return Response({"res": "Object deleted"}, status=status.HTTP_200_OK)