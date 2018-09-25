from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home-page'),
    path('', views.home, name='home'),
    path('data/', views.test, name='test'),
]
