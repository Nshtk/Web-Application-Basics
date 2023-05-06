from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from mainapp import models
from django.db.models import Q
from django.views.generic import TemplateView
from django.core import serializers


class MainPage(TemplateView):
    template_name = 'index.html'


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
                product = models.Product.objects.create(name="Giga bed", description="That's a bed", manufacturer=models.Manufacturer.objects.get(name="Orange brothers factory"), price=500,
                                                             image=None)
                product.furniture_type.set(models.FurnitureType.objects.filter(name="Chair"))
                return JsonResponse(serializers.serialize(product), safe=False)

