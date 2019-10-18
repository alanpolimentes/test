from django.urls import path
from app import views

urlpatterns = [
    path('', views.pushData.as_view(), name='index'),
    path('firstPetition/', views.firstPetition.as_view(), name='test'),
    path('solicitudes/', views.allUsers.as_view({'get': 'get'}), name='all'),
    path('solicitud/<int:id>/', views.specificUser.as_view({'get': 'get'}), name='specificGet'),
    path('solicitud/', views.specificUser.as_view({'post': 'post'}), name='specificPost'),
    path('products/', views.AllProducts.as_view({'get': 'get'}), name='products'),

]