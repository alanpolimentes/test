from django.urls import path
from app import views

urlpatterns = [
    path('', views.Hi.as_view(), name='index'),
    path('firstPetition/', views.firstPetition.as_view(), name='test'),
]