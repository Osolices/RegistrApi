from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


@csrf_exempt
def index(request):
    # Definir las variables
    selectedDay = request.GET.get("day", "todos")
    profesor = "Victor Falso"

    # Definir el array de clases
    clases = [
        {
            "profesor": "Víctor Andrade",
            "dias": "lunes",
            "bloque": "8:30-9:40",
            "ramo": "Calidad de software",
            "seccion": "005D",
        },
        {
            "profesor": "Víctor Andrade",
            "dias": "martes",
            "bloque": "8:30-9:40",
            "ramo": "Diseño y prototipos",
            "seccion": "001D",
        },
        {
            "profesor": "Víctor Andrade",
            "dias": "miercoles",
            "bloque": "10:40-12:50",
            "ramo": "Arquitectura",
            "seccion": "004D",
        },
        {
            "profesor": "Víctor Andrade",
            "dias": "martes",
            "bloque": "10:00-12:50",
            "ramo": "Base de Datos",
            "seccion": "004D",
        },
        {
            "profesor": "Víctor Andrade",
            "dias": "lunes",
            "bloque": "10:00-12:50",
            "ramo": "Calidad de software",
            "seccion": "007D",
        },
        {
            "profesor": "Víctor Andrade",
            "dias": "miercoles",
            "bloque": "11:30-12:50",
            "ramo": "Arquitectura",
            "seccion": "005D",
        },
        {
            "profesor": "Víctor Andrade",
            "dias": "jueves",
            "bloque": "8:30-11:20",
            "ramo": "Arquitectura",
            "seccion": "006D",
        },
        {
            "profesor": "Víctor Andrade",
            "dias": "viernes",
            "bloque": "10:00-12:50",
            "ramo": "Base de Datos",
            "seccion": "004D",
        },
        {
            "profesor": "Víctor Andrade",
            "dias": "jueves",
            "bloque": "13:00-14:20",
            "ramo": "Calidad de software",
            "seccion": "005D",
        },
    ]

    # Filtrar las clases basándose en el día seleccionado
    if selectedDay != "todos":
        clases = [c for c in clases if c["dias"] == selectedDay]

    # Si la solicitud es AJAX, devuelve un JsonResponse
    if is_ajax(request):
        return JsonResponse({"clases": clases})

    # Si no es AJAX, renderiza la página normalmente
    context = {"clases": clases, "selectedDay": selectedDay, "profesor": profesor}
    return render(request, "dashboardprofesor.html", context)


def detalle(request):
    ramo = ""
    selectedRow = {"estado": False}
    clases = [
        {"id": 1, "fecha": "21/09/2023", "estado": True},
        {"id": 2, "fecha": "28/09/2023", "estado": True},
        {"id": 3, "fecha": "05/10/2023", "estado": True},
        {"id": 4, "fecha": "12/10/2023", "estado": True},
        {"id": 5, "fecha": "19/10/2023", "estado": True},
        {"id": 6, "fecha": "26/10/2023", "estado": False},
    ]

    context = {"ramo": ramo, "selectedRow": selectedRow, "clases": clases}

    return render(request, "detalle_ramo.html", context)
