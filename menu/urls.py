from django.urls import path
from . import views

urlpatterns = [
    path('', views.pizza_list, name='pizza_list'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
    path('terms/', views.terms, name='terms'),  # 👈 ADD THIS
    path('proceed-to-payment/', views.proceed_to_payment, name='proceed_to_payment'),
     path('cart/instructions/', views.process_special_instructions, name='process_special_instructions'),

]
