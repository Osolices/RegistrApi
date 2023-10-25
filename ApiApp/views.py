from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Alumno, Asignatura, Asistencia, Clase, Profesor, Sala, Seccion
from .serializers import (
    AlumnoSerializer,
    AsignaturaSerializer,
    AsistenciaSerializer,
    ClaseSerializer,
    ProfesorSerializer,
    SalaSerializer,
    SeccionSerializer,
)


class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

    @action(detail=True, methods=["get"])
    def llamar_api(self, request, pk=None):
        alumno = self.get_object()
        serializer = self.get_serializer(alumno)
        return Response(serializer.data)


class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer

    @action(detail=True, methods=["get"])
    def llamar_api(self, request, pk=None):
        asignatura = self.get_object()
        serializer = self.get_serializer(asignatura)
        return Response(serializer.data)


class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer

    @action(detail=True, methods=["get", "post", "put"])
    def llamar_api(self, request, pk=None):
        if request.method == "GET":
            asistencia = self.get_object()
            serializer = self.get_serializer(asistencia)
            return Response(serializer.data)

        elif request.method == "POST":
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        elif request.method == "PUT":
            asistencia = self.get_object()
            serializer = self.get_serializer(asistencia, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class ClaseViewSet(viewsets.ModelViewSet):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer

    @action(detail=True, methods=["get", "post", "put"])
    def ingresar_datos(self, request, pk=None):
        if request.method == "GET":
            clase = self.get_object()
            serializer = self.get_serializer(clase)
            return Response(serializer.data)

        elif request.method == "POST":
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        elif request.method == "PUT":
            clase = self.get_object()
            serializer = self.get_serializer(clase, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

    @action(detail=True, methods=["get"])
    def ingresar_datos(self, request, pk=None):
        profesor = self.get_object()
        serializer = self.get_serializer(profesor)
        return Response(serializer.data)


class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

    @action(detail=True, methods=["get"])
    def llamar_api(self, request, pk=None):
        sala = self.get_object()
        serializer = self.get_serializer(sala)
        return Response(serializer.data)


class SeccionViewSet(viewsets.ModelViewSet):
    queryset = Seccion.objects.all()
    serializer_class = SeccionSerializer

    @action(detail=True, methods=["get"])
    def llamar_api(self, request, pk=None):
        seccion = self.get_object()
        serializer = self.get_serializer(seccion)
        return Response(serializer.data)
