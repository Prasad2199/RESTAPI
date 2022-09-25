
# Create your views here.
from rest_framework import viewsets
from crudapp.serializers import StudentSerializers
from .models import Student
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status


class StudentAPI(APIView):

    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializers(stu)
            return Response (serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializers(stu,many=True)
        return Response (serializer.data)

    def post(self,request,format=None):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializers(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete data updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def patch(self,request,pk,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializers(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk=None,format=None):
        id = pk 
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})






