from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse, Http404


def send_fruits(request):
    fruits = [
        {"name": "Apple", "color": "Red", "weight": "150g"},
        {"name": "Banana", "color": "Yellow", "weight": "120g"},
        {"name": "Orange", "color": "Orange", "weight": "130g"},
        {"name": "Pear", "color": "Green", "weight": "160g"},
        {"name": "Grape", "color": "Purple", "weight": "5g"},
        {"name": "Pineapple", "color": "Brown", "weight": "1200g"},
        {"name": "Strawberry", "color": "Red", "weight": "20g"},
        {"name": "Watermelon", "color": "Green", "weight": "5000g"},
        {"name": "Kiwi", "color": "Brown", "weight": "80g"},
        {"name": "Blueberry", "color": "Blue", "weight": "2g"}
    ]

    if request.method == "GET":
        return JsonResponse(fruits, safe=False)
    raise Http404("Fruit not found")