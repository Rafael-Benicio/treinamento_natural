from argon2 import PasswordHasher
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from .models import Student, TestToDo, ReadyTest,Question, TestQuestions

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
     tests=[ ReadyTest.objects.get(id=student_test.id_test.id) for student_test in student_tests]
     # tests=[ print(student_test.id_test.id) for student_test in student_tests]
     context = {"student_tests": tests}
     return render(request, "school_test/home.html",context)

def student_test(request, id_student,id_test):
     test_inf=ReadyTest.objects.get(id=int(id_test))
     test_questions=TestQuestions.objects.filter(id_test=id_test)
     questions_from_test=[Question.objects.get(id=question_id.id) for question_id in test_questions]
     # [print(question_id) for question_id in test_questions]
     test={'name':test_inf.test_name}
     test['id_student']=id_student
     test['subject']=test_inf.subject
     test['questions']=questions_from_test
     context = {"test": test}
     # {name=test.name}
     return render(request, "school_test/test.html",context)
     