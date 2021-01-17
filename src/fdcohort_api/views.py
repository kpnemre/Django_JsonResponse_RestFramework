from django.shortcuts import render
from django.http import JsonResponse
from fscohort.models import Student

# Create your views here.
def home_api(request):
    data= {
        "name":"emre",
        "adress":"clarusway",
        "skilss":["python", "django"]
    }
    return JsonResponse(data)

def student_list_api(request):
    if request.method =='GET':
        students = Student.objects.all()
        students_count = Student.objects.count()
         # TypeError: Object of type QuerySet is not JSON serializable 
        #  json objesine çeviremiyor. for ile tek tek ulaşmak gerekiyor
        data ={
            "students":students,
            "count":students_count,
        }
        return JsonResponse(data)
     