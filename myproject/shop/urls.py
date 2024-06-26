from django.urls import path
# from .views import cafe , about, login_user, logout_user
from . import views

urlpatterns = [
    path('', views.cafe, name='home'),
    path('about/',views.about , name = 'about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup_user, name='signup'),
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:cat>', views.category, name='category'),
]


