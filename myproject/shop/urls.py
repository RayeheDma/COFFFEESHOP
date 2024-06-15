from django.urls import path,include
from .views import welcome_to_cafe


urlpatterns = [
    path('', welcome_to_cafe),
]
