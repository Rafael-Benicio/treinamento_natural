from argon2 import PasswordHasher
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from .models import Student, TestToDo, ReadyTest

def index(request):
     return render(request, "school_test/index.html")

def user_login_validate(request):
     id_student=request.POST["id_student"]
     try:
          student_entity = Student.objects.get(id=int(id_student))
          if student_entity.password != request.POST['password']:
               raise "Wrong Password"
     except:
          return render(request,"school_test/index.html",{"error_message": "Seu Id ou Senha estão errados",},)
     else:
          return HttpResponseRedirect(reverse("school_test:home",args=(id_student,)))



def home(request, id_student):
     student_tests=TestToDo.objects.filter(id_student=id_student)
     tests=[ ReadyTest.objects.get(id=student_test.id_test) for student_test in student_tests]
     context = {"student_tests": tests}
     return render(request, "school_test/home.html",context)
