from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import UserCredentials
from .serializers import UserSerializer


class UserCreatListView(generics.ListCreateAPIView):
	queryset = UserCredentials.objects.all()
	serializer_class = UserSerializer

	def delete(self, request):
		UserCredentials.objects.all().delete()
		return Response(status=status.HTTP_204_NO_CONTENT)