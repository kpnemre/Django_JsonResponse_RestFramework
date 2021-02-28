from django.core import serializers
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from rest_framework.views import APIView
from fscohort.models import Student
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import StudentSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
def home_api(request):
    data= {
        "name":"emre",
        "adress":"clarusway",
        "skilss":["python", "django"]
    }
    return JsonResponse(data)

# class StudentList(ListAPIView):
#     queryset= Student.objects.all()
#     serializer_class =StudentSerializer

# class StudentList(CreateAPIView):
#     queryset= Student.objects.all()
#     serializer_class =StudentSerializer
    
class StudentCreate(ListCreateAPIView):
    queryset= Student.objects.all()
    serializer_class =StudentSerializer
        
class StudentGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset= Student.objects.all()
    serializer_class =StudentSerializer
    lookup_field='id'
# ----------------------------------------------------------------------
# 3. restframework
# functional based

# @api_view(["GET", "POST"])
# Browserable api kullanmak için yazdık. Decorator
# def student_list_create_api(request):
#     #tek api ile get ve post yapıyoruz. get ise listele post ise create et.
#     if request.method=="GET":
#         students=Student.objects.all()
#         serializer= StudentSerializer(students, many=True) #many birden fazla obje olursa ekleniyor
#         #içindeki bilgiye serializer.data ile ulaşılıyor
#         return Response(serializer.data)
    
#     elif request.method=="POST":
#         # post_data= json.loads(request.body) burdaki işlemi yapıyor. Burada json veirisini pyhton verisine yani dictionary e çeviriyor.
#         serializer= StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             # kendiliğinden default valdation sağlıyor
#             # student=form.save(commit=False)
#             # student.teacher=request.user
#             # student.save()
#             # Bu işlem yerine:
#             # serializer.save(teacher=request.user)
#             serializer.save()
#             data={
#                 "message":"Student created successfully.. "
#             }
#             return Response(data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    
# # functional based
# # api_view decorater olarak kullanıyoruz
# @api_view(["GET", "PUT","DELETE"])#decorater
# def student_get_update_delete(request,id):
#     # pk: primary key
#     student= get_object_or_404(Student, id=id)
#     if request.method=="GET":
#         serializer= StudentSerializer(student)
#         return Response(serializer.data)
#     if request.method=="PUT": #UPDATE ediyoruz
#         serializer= StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data={
#                 "message":"Student updated succcesffuly"
#             }
#             return Response(data)
#         # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     if request.method=="DELETE":
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
  
  
    
# --------------------------------------------------------
# class based
# APIView den inherit ediyoruz.


# class StudentList(APIView):
#     def get(self,id): # get methodu olduğunu anlıyor
#         students= get_object_or_404(Student, id=id)
#         serializer= StudentSerializer(students, many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer= StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class StudentGetUpdateDelete(APIView):
    
    
#     def get_object(self,id): # get methodu olduğunu anlıyor
#         try:
#             return Student.objects.get(id=id)
#         except Student.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
    
#     def get(self,request,id):
        
#         # student= get_object_or_404(Student, id=id)
#         student= self.get_object(id)
#         serializer= StudentSerializer(student)
#         return Response(serializer.data)
    
#     def put(self,request,id):
#         student= self.get_object(id)
#         serializer= StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save() 
#             data={
#                 "message":"Student updated succcesffuly"
#             }           
#             return Response(data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,id):
#         student= self.get_object(id)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
#-----------------------------------------------------------------------------------------       
        

# 1. yöntem Jsonresponse kullanıp queryset elde edip for ile dönüp manuel Json üretmek 
# dinamik bir yöntem değil, database de ki veriyi göndermiyor

# def student_list_api(request):
#     if request.method =='GET':
#         students = Student.objects.all()#query set döner . for ile tek tek almak gerekir
#         students_count = Student.objects.count()
#          # TypeError: Object of type QuerySet is not JSON serializable 
#         #  json objesine çeviremiyor. for ile tek tek ulaşmak gerekiyor
#         student_list =[]
#         for student in students:
#             student_list.append({
#                 "firstname":student.first_name,
#                 "lastname":student.last_name,
#                 "number":student.number,
#             })
#         data ={
#             # "students":students,
#             "students":student_list,
#             "count":students_count,
#         }
#         return JsonResponse(data)
     

# 2. yöntem serialize kullanmak . bu queryset i otomatik istenen formata çeviriyor. Sözlük üzerinde çalışmamız gerek. 
# def student_list_api(request):
#     if request.method =='GET':
#         students = Student.objects.all()
#         students_count = Student.objects.count()
#         student_data = serialize("python", students)
#         data ={
#             "students":student_data,
#             "count":students_count,
#         }
#         return JsonResponse(data)

#3. yöntem
# @csrf_exempt
# def student_create_api(request):
#     if request.method =='POST':
#         post_data= json.loads(request.body)#dictionary formatına çevrildi
        
#         name= post_data.get("first_name")
#         lastname= post_data.get("last_name")
#         number = post_data.get("number")
#         student_data ={
#             "first_name":name,
#             "last_name":lastname,
#             "number":number,
#         } 
#         student_obj =Student.objects.create(**student_data) 
#         #( "first_name":name, "last_name":lastname,....)
#         data={
#             # "message":"Student created successfully"
#             "message": f"Student created successfully{student_obj.first_name}"
#         }
#         print(student_data)
#         return JsonResponse(data, status=201)