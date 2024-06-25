from django.urls import path
from .views import cafe

urlpatterns = [
    path('', cafe, name='home'),

]
