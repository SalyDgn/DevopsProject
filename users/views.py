from django.shortcuts import render
from .models import User, Visit
from .serializers import UserSerializer, VisitSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.


def home(request):
    visit = Visit.objects.all()
    if len(visit) == 0:
        Visit.objects.create(count=1)
    else:
        visit = Visit.objects.first()
        visit.count += 1
        visit.save()
    return render(request, "home.html")


class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class VisitCountView(APIView):
    def get(self, request):
        visits = Visit.objects.all()
        serializer = VisitSerializer(visits, many=True)
        return Response(serializer.data)
