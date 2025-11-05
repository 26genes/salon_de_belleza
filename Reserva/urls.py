from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registrar_usuario, name='registrar_usuario'),
    path('login/', views.login_usuario, name='login_usuario'),
    path('', views.inicio_cliente, name='inicio_cliente'),
    path('redirigir/', views.redirigir_tipo_usuario, name='redirigir_tipo_usuario'),
    path('logout/', views.log_out_user, name='log_out_user'),
    path('create/', views.create_servicio, name='create_servicio'),
    path('mis_reservas/', views.ver_reservas, name='ver_reservas'),
    path('mis_reservas/<int:id>/', views.reserva_detalle, name='reserva_detalle'),
    path('mis_reservas/<int:id>/update/', views.actualizar_reserva, name='actualizar_reserva'),
    path('mis_reservas/<int:id>/delete/', views.eliminar_reserva, name='eliminar_reserva'),
    path('servicios/',views.ver_servicio, name= 'ver_servicio')
]
