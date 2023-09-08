from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET
from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings


# Create your views here.


def home(request):
    settings.VISIT_COUNT += 1
    return HttpResponse('<h1>Welcome!</h1>')


class UserListView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class VisitCountView(APIView):
    def get(self, request):
        # Récupérez le nombre de visites à partir des paramètres de configuration
        visit_count = settings.VISIT_COUNT
        return Response({'visit_count': visit_count})
