from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.

class CancionView(APIView):
    def get(self,request):
        dataCancion = Cancion.objects.all()
        serCancion = CancionSerializer(dataCancion,many=True)
        return Response({'ok':True,
                         'content':serCancion.data})
        
    def post(self,request):
        serCancion = CancionSerializer(data=request.data)
        serCancion.is_valid(raise_exception=True)
        serCancion.save()
        
        return Response({'ok':True,
                         'content':serCancion.data})
        
class ActualizarView(APIView):
    def put(self,request,cancion_id):
        dataCancion = Cancion.objects.get(pk=cancion_id)
        serCancion = CancionSerializer(dataCancion,data=request.data)
        serCancion.is_valid(raise_exception=True)
        serCancion.save()
        return Response({'ok':True,
                        'content':serCancion.data})
class DeleteView(APIView):
    def delete(self,request,cancion_id):
        dataCancion = Cancion.objects.get(pk=cancion_id)
        dataCancion.delete()
        return Response({'ok':True,
                         'content':'Cancion eliminada'})
        