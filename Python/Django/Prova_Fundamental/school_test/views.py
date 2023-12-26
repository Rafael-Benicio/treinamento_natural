from argon2 import PasswordHasher
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from .models import Student
from .module.build_and_calculate import *

def index(request)->HttpResponse:
     return render(request, "school_test/index.html")

def user_login_validate(request)->HttpResponse:
     ph = PasswordHasher()
     id_student=request.POST["id_student"]
     try:
          student_entity = Student.objects.get(id=int(id_student))
          if not (ph.verify(student_entity.password, request.POST['password'])):
               raise "Wrong Password"
     except:
          return render(request,"school_test/index.html",{"error_message": "Seu Id ou Senha estão errados","current_id":request.POST["id_student"],"current_password":request.POST["password"]})
     else:
          return HttpResponseRedirect(reverse("school_test:home",args=(id_student,)))

def home(request, id_student:int)->HttpResponse:
     context = {"student_tests": build_list_of_tests(id_student)}
     return render(request, "school_test/home.html",context)

def student_test(request, id_student:int,id_test:int)->HttpResponse:
     context = {"test": build_student_test(id_student,id_test)}
     return render(request, "school_test/test.html",context)

def result_calculate(request)->HttpResponse:
     grade=calculate_test_grade(remove_identification_data(request.POST))
     regist_student_test_grade(request.POST,grade)
     return HttpResponseRedirect(reverse("school_test:home",args=(request.POST["id_student"],)))