from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Question)
admin.site.register(ReadyTest)
admin.site.register(TestQuestions)
admin.site.register(Student)
admin.site.register(StudentClass)
admin.site.register(TestToDo)