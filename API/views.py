from rest_framework import viewsets, status, mixins, generics
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.request import Request
from django.shortcuts import render
from .serializer import *
from Core.models import *


User = get_user_model()

# Generic view
class TodosGenericApiView(generics.ListCreateAPIView):
    queryset = User.objects.order_by('id').all()
    serializer_class = UserSerializer


# Mixin View
class TodosListMixinApiView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = ToDoModel.objects.order_by('id').all()
    serializer_class = TodosSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request: Request):
        print(self.serializer_class.data)
        return self.create(request)


# Mixin View
class TodosDetailMixinApiView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = ToDoModel.objects.order_by('id').all()
    serializer_class = TodosSerializer

    def get(self, request: Request, pk):
        return self.retrieve(request, pk)

    def put(self, request: Request, pk):
        return self.update(request, pk)

    def delete(self, request: Request, pk):
        return self.destroy(request, pk)

