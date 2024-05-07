from rest_framework import serializers
from .models import UserCredentials

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=UserCredentials
		fields='__all__'