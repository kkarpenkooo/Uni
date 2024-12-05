from django.urls import path
from . import views

urlpatterns = [
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('materials/', views.material_list, name='material_list'),
    path('supplies/', views.supply_list, name='supply_list'),
]
