from django.urls import path
from .views import cafe , about

urlpatterns = [
    path('', cafe, name='home'),
    path('about/',about , name = 'about'),

]
