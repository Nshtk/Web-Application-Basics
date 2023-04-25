from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods


# def Root(request)
#     return HttpResponse()
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


@require_http_methods(["GET", "POST"])
def item(request):
    return JsonResponse({"sample": "1", "sample2": 2})
