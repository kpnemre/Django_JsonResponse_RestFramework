from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from fscohort.forms import StudentForm
from .models import Student
# Create your views here.

# def home_view (request):
#     return HttpResponse("hi, this is function")

def about_view (request):
    return HttpResponse("hi, this is About page")

def home_view(request):
    # print(request.GET.get("q"))
    # print(request.COOKIES)
    # print(request.user)
    # print(request.path)
    
    # form= StudentForm()
    # my_content ={
    #     'title': 'clarusway',
    #     'dict_1':{'django':'best framework'},
    #     'my_list':[1,2,3,4,5],  
    #     'form':form
    #     }
    # return render(request, "fscohort/home.html",my_content)
    return render(request, "fscohort/home.html")

def student_list(request):
    students= Student.objects.all()
    context= {
        'students':students
    }
    return render(request,"fscohort/student_list.html", context)

def student_add(request):
    form = StudentForm()
    if request.method == "POST":
        print(request.POST)
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect("home")
            return redirect("add")

    context = {
        'form': form
    }
    return render(request, "fscohort/student_add.html", context)

def student_detail(request, id):
    # student= Student.objects.get(id=id)
    student = get_object_or_404(Student, id=id)
    
    context ={
       'student': student
    }
    return render(request, "fscohort/student_detail.html", context)

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect("list")
    return render(request, "fscohort/student_delete.html")


def student_update(request,id):
    # student= Student.objects.get(id=id)
    student = get_object_or_404(Student, id=id)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        # formun içindeki bilgileri getir
        if form.is_valid():
            form.save()
            # return redirect("home")
            return redirect("list")
    context={
        'student':student,
        'form':form
    }
    return render(request, "fscohort/student_update.html", context)
    
