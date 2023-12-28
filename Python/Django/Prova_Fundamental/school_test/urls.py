from django.urls import path

import school_test.views

app_name="school_test"

urlpatterns = [
    path("", school_test.views.login, name="login"),
    path("validate_user/", school_test.views.user_login_validate, name="validate"),
    path("result/", school_test.views.result_calculate, name="result"),
    path("<int:id_student>/home/", school_test.views.home, name="home"),
    path("<int:id_student>/home/prova/<int:id_test>", school_test.views.student_test, name="test"),
    # path("<int:id_student>/test/", school_test.views.home, name="home"),
]