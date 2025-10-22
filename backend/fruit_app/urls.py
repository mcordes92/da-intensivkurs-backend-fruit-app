from django.urls import path
from .views import send_fruits, info_page

app_name = 'fruit_app' 

urlpatterns = [
    path('', send_fruits),
    path('info/', info_page),
]