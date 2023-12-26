from argon2 import PasswordHasher
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from .models import Student, TestToDo, ReadyTest,Question, TestQuestions

def index(request):
     return render(request, "school_test/index.html")

def user_login_validate(request):
     ph = PasswordHasher()
     id_student=request.POST["id_student"]
     try:
          student_entity = Student.objects.get(id=int(id_student))
          # if student_entity.password != request.POST['password']:
          if not (ph.verify(student_entity.password, request.POST['password'])):
               raise "Wrong Password"
     except:
          return render(request,"school_test/index.html",{"error_message": "Seu Id ou Senha estão errados","current_id":request.POST["id_student"],"current_password":request.POST["password"]})
     else:
          return HttpResponseRedirect(reverse("school_test:home",args=(id_student,)))



def home(request, id_student)->HttpResponse:
     associated_tests=[]
     id_from_student_and_readytests=TestToDo.objects.filter(id_student=id_student)
     for testtodo_object in id_from_student_and_readytests:
          test_entity=(ReadyTest.objects.get(id=testtodo_object.id_test.id))

          test_object={"test_name":test_entity.test_name}
          test_object["subject"]=test_entity.subject
          test_object["id"]=test_entity.id
          test_object["grade"]=testtodo_object.grade
          test_object["was_done"]=testtodo_object.was_done

          associated_tests.append(test_object)

     context = {"student_tests": associated_tests}
     return render(request, "school_test/home.html",context)

def student_test(request, id_student,id_test):
     questions=[]
     student_test=ReadyTest.objects.get(id=int(id_test))

     id_from_question_and_readytest=TestQuestions.objects.filter(id_test=id_test)
     for testquestion_object in id_from_question_and_readytest:
          questions.append(Question.objects.get(id=testquestion_object.id_question.id))

     test={'name':student_test.test_name, }
     test['id_student']=id_student
     test['id_test']=id_test
     test['subject']=student_test.subject
     test['questions']=questions

     context = {"test": test}

     # {name=test.name}
     return render(request, "school_test/test.html",context)

def result_calculate(request):
     grade=calculate_test_grade(remove_identification_data(request.POST))
     student_test=TestToDo.objects.get(id_test=int(request.POST["id_test"]), id_student=int(request.POST["id_student"]))
     student_test.grade=grade
     student_test.was_done=True
     student_test.save()
     return HttpResponseRedirect(reverse("school_test:home",args=(request.POST["id_student"],)))

def calculate_test_grade(id_question_and_choice:dict)-> float:
     weight=10/len(id_question_and_choice)
     right_answers=0

     for id_question in id_question_and_choice: 
          asw=Question.objects.get(id=id_question).answer
          if asw==int(id_question_and_choice[id_question]):
               right_answers+=1
     
     return right_answers*weight

def remove_identification_data(test_form:dict)->dict:
     return {field_name:test_form[field_name] for field_name in test_form if field_name!='id_student' and field_name!='csrfmiddlewaretoken' and field_name!='id_test'}
    
