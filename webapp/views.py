from django.views.generic import UpdateView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import employees, CHAMBRE
from .models import reservation
from .models import CHAMBREDEP
from .models import CHAMBREARR
from .models import CHAMBREHORS

from .serializers import reservationSerializer, CHAMBREDEPSerializer, CHAMBREHORSSerializer, CHAMBRESerializer
from .serializers import CHAMBREARRSerializer
from .serializers import employeesSerializer

from rest_framework.decorators import api_view
from django.views.generic.list import ListView


@api_view(['GET'])
def employeesList(request):
    employees1 = employees.objects.all()
    serializer = employeesSerializer(employees1, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def employeesdetail(request, pk):
    try:
        employees1 = employees.objects.get(id=pk)
    except:
        return Response('reponse vide pour ' + str(pk))
    serializer = employeesSerializer(employees1)
    return Response(serializer.data)


@api_view(['POST'])
def employeesCreate(request):
    serializer = employeesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def employeesupdate(request, pk):
    try:
        employees1 = employees.objects.get(id=pk)
    except:
        return Response('reponse vide pour ' + str(pk))
    serializer = employeesSerializer(instance=employees1, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def employeesdelete(request, pk):
    employees1 = employees.objects.get(id=pk)
    try:
        employees1 = employees.objects.get(id=pk)
    except:
        return Response('reponse vide pour ' + str(pk))
    serializer = employeesSerializer(employees1)
    employees1.delete()
    return Response('delete')


# -------------------------------RESERVATION----------------------------------

@api_view(['GET'])
def reservationList(request):
    reservation1 = reservation.objects.all()
    serializer = reservationSerializer(reservation1, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def reservationdetail(request, pk):
    try:
        reservation1 = reservation.objects.get(id=pk)
    except:
        return Response('reponse vide pour ' + str(pk))
    serializer = reservationSerializer(reservation1)
    return Response(serializer.data)


@api_view(['POST'])
def reservationCreate(request):
    serializer = reservationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def reservationupdate(request, pk):
    try:
        reservation1 = reservation.objects.get(id=pk)
    except:
        return Response('reponse vide pour ' + str(pk))
    serializer = employeesSerializer(instance=reservation1, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def reservationdelete(request, pk):
    reservation1 = reservation.objects.get(id=pk)
    try:
        reservation1 = reservation.objects.get(id=pk)
    except:
        return Response('reponse vide pour ' + str(pk))
    serializer = reservationSerializer(reservation1)
    reservation1.delete()
    return Response('delete')


# -------------------------------ARRIVE--------------------------------------------------

@api_view(['GET'])
def arriveelist(request):
    CHAMBREARR1 = CHAMBREARR.objects.all()
    serializer = CHAMBREARRSerializer(CHAMBREARR1, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def arriveedetail(request, pk):
    try:
        CHAMBREARR1 = CHAMBREARR.objects.get(id=pk)
    except:
        return Response('reponse vide pour ' + str(pk))
    serializer = CHAMBREARRSerializer(CHAMBREARR1)
    return Response(serializer.data)


@api_view(['GET'])
def arriveetrier(request, debut, fin):
    try:
        CHAMBREARR1 = CHAMBREARR.objects.filter(CHAMBREARR.date_arr >= debut, CHAMBREARR.date_dep <= fin)
    except:
        return Response('réponse vide entre les deux date ' + str(debut) + ' et ' + str(fin))
    serializer = CHAMBREARRSerializer(CHAMBREARR1)
    return Response(serializer.data)


# -----http://127.0.0.1:8000/triearr/2019-03-01/2019-03-01/

@api_view(['POST'])
def arriveeCreate(request):
    serializer = CHAMBREARRSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def arriveeupdate(request, pk):
    try:
        CHAMBREARR1 = CHAMBREARR.objects.get(id=pk)
    except:
        return Response('reponse vide pour ' + str(pk))
    serializer = CHAMBREARRSerializer(instance=CHAMBREARR1, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def arriveedelete(request, pk):
    try:
        CHAMBREARR1 = CHAMBREARR.objects.get(id=pk)
    except:
        return Response('reponse vide pour ' + str(pk))
    serializer = reservationSerializer(CHAMBREARR1)
    CHAMBREARR1.delete()
    return Response('delete')


# -------------------------------DEPART--------------------------------------------------
@api_view(['GET'])
def departlist(request):
    CHAMBREDEP1 = CHAMBREDEP.objects.all()
    serializer = CHAMBREDEPSerializer(CHAMBREDEP1, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def departdetail(request, pk):
    try:
        CHAMBREDEP1 = CHAMBREDEP.objects.get(id=pk)
    except:
        return Response('reponse vide pour ' + str(pk))
    serializer = CHAMBREDEPSerializer(CHAMBREDEP1)
    return Response(serializer.data)


@api_view(['GET'])
def departtrier(request, debut, fin):
    try:
        CHAMBREDEP1 = CHAMBREDEP.objects.filter(CHAMBREDEP.date_arr >= debut, CHAMBREDEP.date_dep <= fin)
    except:
        return Response('réponse vide entre les deux date ' + str(debut) + ' et ' + str(fin))
    serializer = CHAMBREARRSerializer(CHAMBREDEP1)
    return Response(serializer.data)


# -----http://127.0.0.1:8000/triearr/2019-03-01/2019-03-01/


@api_view(['POST'])
def departCreate(request):
    serializer = CHAMBREDEPSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def departupdate(request, pk):
    try:
        CHAMBREDEP1 = CHAMBREDEP.objects.get(id=pk)
    except:
        return Response('reponse vide pour ' + str(pk))
    serializer = CHAMBREDEPSerializer(instance=CHAMBREDEP1, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def departdelete(request, pk):
    try:
        CHAMBREDEP1 = CHAMBREDEP.objects.get(id=pk)
    except:
        return Response('reponse vide pour ' + str(pk))
    serializer = reservationSerializer(CHAMBREDEP1)
    CHAMBREDEP1.delete()
    return Response('delete')


# -------------------------------HORS SERVICE--------------------------------------------------

@api_view(['GET'])
def horsservicelist(request):
    horsservice1 = CHAMBREHORS.objects.all()
    serializer = CHAMBREHORSSerializer(horsservice1, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def horsservicedetail(request, pk):
    try:
        horsservice1 = CHAMBREHORS.objects.get(id=pk)
    except:
        return Response('reponse vide pour ' + str(pk))
    serializer = CHAMBREHORSSerializer(horsservice1)
    return Response(serializer.data)


@api_view(['GET'])
def horsservicetrier(request, debut, fin):
    try:
        horsservice1 = CHAMBREHORS.objects.filter(CHAMBREHORS.date_arr >= debut, CHAMBREHORS.date_dep <= fin)
    except:
        return Response('réponse vide entre les deux date ' + str(debut) + ' et ' + str(fin))
    serializer = CHAMBREHORSSerializer(horsservice1)
    return Response(serializer.data)


# -----http://127.0.0.1:8000/triearr/2019-03-01/2019-03-01/


@api_view(['POST'])
def horsservicecreate(request):
    serializer = CHAMBREHORSSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def horsserviceupdate(request, pk):
    try:
        horsservice1 = CHAMBREHORS.objects.get(id=pk)
    except:
        return Response('reponse vide pour ' + str(pk))
    serializer = CHAMBREARRSerializer(instance=horsservice1, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def horsservicedelete(request, pk):
    try:
        horsservice1 = CHAMBREHORS.objects.get(id=pk)
    except:
        return Response('reponse vide pour ' + str(pk))
    serializer = reservationSerializer(horsservice1)
    horsservice1.delete()
    return Response('delete')


# -------------------------------CHAMBRE LIBRE--------------------------------------------------

@api_view(['GET'])
def chambretlist(request):
    CHAMBRE1 = CHAMBRE.objects.all()
    serializer = CHAMBRESerializer(CHAMBRE1, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def chambredetail(request, pk):
    try:
        CHAMBRE1 = CHAMBRE.objects.get(libre=pk)
    except:
        return Response('reponse vide pour ' + str(pk))
    serializer = CHAMBREDEPSerializer(CHAMBRE1, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def chambrecreate(request):
    serializer = CHAMBRESerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def chambreupdate(request, pk):
    try:
        CHAMBRE1 = CHAMBRE.objects.get(id=pk)
    except:
        return Response('reponse vide pour ' + str(pk))
    serializer = CHAMBRESerializer(instance=CHAMBRE, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def chambredelete(request, pk):
    try:
        CHAMBRE1 = CHAMBRE.objects.get(id=pk)
    except:
        return Response('reponse vide pour ' + str(pk))
    serializer = reservationSerializer(CHAMBRE1)
    CHAMBRE1.delete()
    return Response('delete')
