from django.urls import path

import school_test.views

app_name="school_test"

urlpatterns = [
    path("", school_test.views.index, name="index"),
]