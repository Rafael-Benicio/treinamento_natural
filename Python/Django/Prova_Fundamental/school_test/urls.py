from django.urls import path

import school_test.views

app_name="school_test"

urlpatterns = [
    path("", school_test.views.index, name="index"),
    path("validate_user/", school_test.views.user_login_validate, name="validate"),
    path("<int:id_student>/home/", school_test.views.home, name="home"),
    # path("<int:id_student>/test/", school_test.views.home, name="home"),
]