from rest_framework.views import APIView
from rest_framework.response import Response

#*Para autenticacion
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class IndexView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        context = {
            'ok': True,
            'message': 'El servidor está activo!',
            'user':str(request.user)
        }
        return Response(context)
