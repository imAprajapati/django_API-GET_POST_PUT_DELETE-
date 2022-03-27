from functools import partial
from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
def student(request):
    # print('hello')
    if request.method=='GET':
        # print('this is get')
        id=request.data.get('id',None)
        # print('the value of id=',id)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created successfully !!'})
        return Response(serializer.errors)

    elif request.method=='PUT':
        id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data upadated successfully !!'})
        return Response(serializer.errors)
    elif request.method=='DELETE':
        id=request.data.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'data deleted successfully !!'})