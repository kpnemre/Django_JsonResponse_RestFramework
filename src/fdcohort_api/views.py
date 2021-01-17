from django.shortcuts import render
from django.http import JsonResponse
from fscohort.models import Student
from django.core.serializers import serialize

# Create your views here.
def home_api(request):
    data= {
        "name":"emre",
        "adress":"clarusway",
        "skilss":["python", "django"]
    }
    return JsonResponse(data)

# 2. yöntem serialize kullanmak . bu queryset i otomatik istenen formata çeviriyor. Sözlük üzerinde çalışmamız gerek. 
def student_list_api(request):
    if request.method =='GET':
        students = Student.objects.all()
        students_count = Student.objects.count()
        student_date = serialize("python", students)
        data ={
            "students":student_date,
            "count":students_count,
        }
        return JsonResponse(data)





















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
     