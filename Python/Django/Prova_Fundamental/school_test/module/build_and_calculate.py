from ..models import Student, TestToDo, ReadyTest,Question, TestQuestions

def calculate_test_grade(id_question_and_choice:dict)-> float:
     weight=10/len(id_question_and_choice)
     right_answers=0

     for id_question in id_question_and_choice: 
          asw=Question.objects.get(id=id_question).answer
          if asw==int(id_question_and_choice[id_question]):
               right_answers+=1
     
     return right_answers*weight

def regist_student_test_grade(test_form:dict,grade:float)->None:
     student_test=TestToDo.objects.get(id_test=int(test_form["id_test"]), id_student=int(test_form["id_student"]))
     if not (student_test.was_done):
          student_test.grade=grade
          student_test.was_done=True
          student_test.save()

def remove_identification_data(test_form:dict)->dict:
     return {field_name:test_form[field_name] for field_name in test_form if field_name!='id_student' and field_name!='csrfmiddlewaretoken' and field_name!='id_test'}
    
def build_list_of_tests(id_student:int)-> list[dict]:
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
     return associated_tests

def build_student_test(id_student:int,id_test:int)->dict:
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
     return test