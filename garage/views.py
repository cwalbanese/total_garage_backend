from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken, RepairSerializer
from .models import Repair

# Repair model API view for GET and POST requests from frontend

class RepairList(generics.ListCreateAPIView):
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer

# Repair model API view for GET, PUT, DELETE requests from frontend
class RepairSpecific(generics.RetrieveUpdateDestroyAPIView):
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer

# JWT Authentication, find out who current user is and return the data to be used on frontend

@api_view(['GET'])
def current_user(request):
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


# JWT Authentication, create a new user

class UserList(APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
