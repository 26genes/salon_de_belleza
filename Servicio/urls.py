from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('registrar/', views.registrar_admin, name='registrar_admin'),
    path('inicio/', views.inicio_admin, name='inicio_admin'),
    path('crear_servicio/', views.crear_servicio, name='crear_servicio'),
    path('ver_servicios/', views.ver_servicios, name='ver_servicios'),
    path('ver_servicios/<int:id>/', views.servicio_detalle, name='servicio_detalle'),
    path('ver_servicios/<int:id>/update/', views.actualizar_servicio, name='actualizar_servicio'),
    path('ver_servicios/<int:id>/delete/', views.eliminar_servicio, name='eliminar_servicio'),
    path('reservas/', views.ver_reservas, name='ver_reservas'),
]


# Servir archivos de medios durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)