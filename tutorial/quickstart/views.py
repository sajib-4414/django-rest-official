from django.shortcuts import render
from django.contrib.auth.models import User, Group
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer
from rest_framework import viewsets

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    api endpoint that allows user to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer