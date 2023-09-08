from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer

# Create your views here.


@require_GET
def get_users(request):
    users = User.objects.values(
        'username', 'email', 'first_name', 'last_name')
    return JsonResponse(list(users), safe=False)


class UserViewset(viewsets.ModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
