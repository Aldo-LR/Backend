from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

class IndexView(APIView):
    
    def get(self,request):
        context = {'ok':True,
                   'message':'el servidor está activo!'
                   }
        return Response(context)
    
class CancionView(APIView):
    def get(self,request):
        dataCancion = Cancion.objects.all()
        serCancion = CancionSerializer(dataCancion,many=True)
        context ={'ok':True,
                'content':serCancion.data}
        return Response(context)

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