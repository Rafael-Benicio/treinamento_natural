from argon2 import PasswordHasher
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from .models import Student
from .module.build_and_calculate import *

def login(request)->HttpResponse:
     return render(request, "school_test/login.html")

def user_login_validate(request)->HttpResponse:
     ph = PasswordHasher()
     id_student=request.POST["id_student"]
     try:
          student_entity = Student.objects.get(id=int(id_student))
          if not (ph.verify(student_entity.password, request.POST['password'])):
               raise "Wrong Password"
     except:
          return render(request,"school_test/login.html",{"error_message": "Seu Id ou Senha estão errados","current_id":request.POST["id_student"],"current_password":request.POST["password"]})
     else:
          response= HttpResponseRedirect(reverse("school_test:home",))
          response.set_cookie('id_student_cookie', request.POST['id_student'])
          return response

def home(request)->HttpResponse:
     id_student= int(request.COOKIES['id_student_cookie'])
     context = {"student_tests": build_list_of_tests(id_student)}
     return render(request, "school_test/home.html",context)

def student_test(request,id_test:int)->HttpResponse:
     id_student= int(request.COOKIES['id_student_cookie'])
     context = {"test": build_student_test(id_student,id_test)}
     return render(request, "school_test/test.html",context)

def result_calculate(request)->HttpResponse:
     grade=calculate_test_grade(remove_identification_data(request.POST))
     regist_student_test_grade(request.POST,grade)
     return HttpResponseRedirect(reverse("school_test:home",))