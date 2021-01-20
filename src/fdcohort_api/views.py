from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from fscohort.models import Student
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import StudentSerializer
# Create your views here.
def home_api(request):
    data= {
        "name":"emre",
        "adress":"clarusway",
        "skilss":["python", "django"]
    }
    return JsonResponse(data)

# 3. restframework
@api_view(["GET", "POST"])
# Browserable api kullanmak için yazdık. 
def student_list_create_api(request):
    if request.method=="GET":
        students=Student.objects.all()
        serializer= StudentSerializer(students, many=True) #many birden fazla obje olursa ekleniyor
        #içindeki bilgiye serializer.data ile ulaşılıyor
        return Response(serializer.data)
    elif request.method=="POST":
        serializer= StudentSerializer(data=request.data)
        # post_data= json.loads(request.body) burdaki işlemi yapıyor
        if serializer.is_valid():
            # kendiliğinden default valdation sağlıyor
            # student=form.save(commit=False)
            # student.teacher=request.user
            # student.save()
            # Bu işlem yerine:
            # serializer.save(teacher=request.user)
            serializer.save()
            data={
                "message":"Student created successfully.. "
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT","DELETE"])#decorater
def student_get_update_delete(request,id):
    # pk: primary key
    student= get_object_or_404(Student, id=id)
    if request.method=="GET":
        serializer= StudentSerializer(student)
        return Response(serializer.data)
    if request.method=="PUT":
        serializer= StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={
                "message":"Student updated succcesffuly"
            }
            return Response(data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method=="DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
       
            
        
    
        
    


# 2. yöntem serialize kullanmak . bu queryset i otomatik istenen formata çeviriyor. Sözlük üzerinde çalışmamız gerek. 
# validation yazmadık
# def student_list_api(request):
#     if request.method =='GET':
#         students = Student.objects.all()
#         students_count = Student.objects.count()
#         student_date = serialize("python", students)
#         data ={
#             "students":student_date,
#             "count":students_count,
#         }
#         return JsonResponse(data)
    
    
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
        

# 1. yöntem Jsonresponse kullanıp queryset elde edip for ile dönüp manuel Json üretmek 


# def student_list_api(request):
#     if request.method =='GET':
#         students = Student.objects.all()
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
     