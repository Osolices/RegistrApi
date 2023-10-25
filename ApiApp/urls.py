from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'alumnos', views.AlumnoViewSet)
router.register(r'asignaturas', views.AsignaturaViewSet)
router.register(r'asistencias', views.AsistenciaViewSet)
router.register(r'clases', views.ClaseViewSet)
router.register(r'profesores', views.ProfesorViewSet)
router.register(r'salas', views.SalaViewSet)
router.register(r'secciones', views.SeccionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]