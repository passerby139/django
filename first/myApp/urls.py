from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index),
    path('grades', views.grades),
    path('students', views.students),
    path('grades/<int:num>', views.gradesStudents)  # 这里的num要与视图中定义的函数形参名字一致
]
