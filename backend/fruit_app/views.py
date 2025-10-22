from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse, Http404


def send_fruits(request):
    fruits = [
        {"name": "Apfel", "weight": 100, "color": "Rot", "ordered": True},
        {"name": "Banane", "weight": 120, "color": "Gelb", "ordered": True},
        {"name": "Orange", "weight": 150, "color": "Orange", "ordered": True},
        {"name": "Birne", "weight": 130, "color": "Grün", "ordered": False},
        {"name": "Kirsche", "weight": 10, "color": "Rot", "ordered": False}
    ]

    if request.method == "GET":
        return render(request, "fruit_app/fruitlist.html", {"fruits": fruits})
    raise Http404("Fruit not found")

def info_page(request):
    return render(request, "fruit_app/info.html")