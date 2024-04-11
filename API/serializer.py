from rest_framework import serializers
from Core.models import *
from django.contrib.auth import get_user_model

User = get_user_model()
class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoModel
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    # nested serializer
    todos = TodosSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = '__all__'



