from django.urls import path
from .views import cafe , about, login_user, logout_user

urlpatterns = [
    path('', cafe, name='home'),
    path('about/',about , name = 'about'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

]


