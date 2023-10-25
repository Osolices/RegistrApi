from django.db.models import fields
from rest_framework import serializers
from .models import Alumno, Asignatura, Asistencia, Clase, Profesor, Sala, Seccion

class AlumnoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alumno
        fields = ['rut_alumno', 'p_nombre', 's_nombre', 'p_apellido', 's_apellido', 'correo', 'telefono', 'carrera', 'pass_field']

class AsignaturaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Asignatura
        fields = ['id_asignatura', 'descripcion']

class AsistenciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Asistencia
        fields = ['id_asistencia', 'fecha', 'estado', 'alumno_rut_alumno', 'clase_id_clase', 'latitud_alumno', 'longitud_alumno']

class ClaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clase
        fields = ['id_clase', 'horario', 'cantidad_alumnos', 'sala_id_sala', 'seccion_id_seccion']

class ProfesorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profesor
        fields = ['rut_profesor', 'p_nombre', 's_nombre', 'p_apellido', 's_apellido', 'correo', 'telefono', 'pass_field']

class SalaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sala
        fields = ['id_sala', 'descripcion', 'longitud', 'latitud']

class SeccionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seccion
        fields = ['id_seccion', 'descripcion', 'asignatura_id_asignatura', 'profesor_rut_profesor']
