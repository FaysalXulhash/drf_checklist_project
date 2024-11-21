from django.shortcuts import render
from rest_framework.views import APIView
from .models import CheckList, CheckListItem
from .serializers import CheckListSerializer, CheckListItemSerializer
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework import status
# Create your views here.

class Test(ListCreateAPIView):
    serializer_class = CheckListSerializer


class CheckListApi(APIView):
    def get(self, request, format=None):
        lists = CheckList.objects.all()
        serializer = CheckListSerializer(lists, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = CheckListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)



class CheckListDetailsApi(APIView):
    serializer_class = CheckListSerializer
    def get(self, request, pk, format=None):
        check_list = CheckList.objects.get(id=pk)
        serializer = CheckListSerializer(check_list)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        check_list = CheckList.objects.get(id=pk)
        serializer = CheckListSerializer(check_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request, pk, format=None):
        check_list = CheckList.objects.get(id=pk)
        serializer = CheckListSerializer(check_list, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        check_list = CheckList.objects.get(id=pk)
        check_list.delete()
        return Response({'msg': 'List deleted!'})


# check list item---------------------

class CheckListItemApi(APIView):
    def post(self, request, format=None):
        serializer = CheckListItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CheckListItemDetailApi(APIView):

    def get(self, request, pk, format=None):
        item = CheckListItem.objects.get(id=pk)
        serializer = CheckListItemSerializer(item)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        item = CheckListItem.objects.get(id=pk)
        serializer = CheckListItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request, pk, format=None):
        item = CheckListItem.objects.get(id=pk)
        serializer = CheckListItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        item = CheckListItem.objects.get(id=pk)
        item.delete()
        return Response({'msg': 'Item deleted successfully!'})
