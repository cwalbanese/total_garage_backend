from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken, YearSerializer, RepairSerializer
from .models import Year, Repair


class YearList(generics.ListCreateAPIView):
    queryset = Year.objects.all()
    serializer_class = YearSerializer

class YearSpecific(generics.RetrieveUpdateDestroyAPIView):
    queryset = Year.objects.all()
    serializer_class = YearSerializer

class RepairList(generics.ListCreateAPIView):
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer

class RepairSpecific(generics.RetrieveUpdateDestroyAPIView):
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer



@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.