from django.urls import path
from app import views

urlpatterns = [
    path('', views.pushData.as_view(), name='index'),
    path('firstPetition/', views.firstPetition.as_view(), name='test'),
    path('solicitudes/', views.allSolicitudes.as_view({'get': 'get'}), name='all'),
    path('solicitud/<int:id>/', views.specificSolicitude.as_view({'get': 'get'}), name='specificGet'),
    path('solicitud/', views.specificSolicitude.as_view({'post': 'post'}), name='specificPost'),
    path('products/', views.AllProducts.as_view({'get': 'get'}), name='products'),

]