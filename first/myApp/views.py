from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("you are so cute!")


# 查看班级表视图
from .models import Grades


def grades(request):
    # 去模板里取数据
    gradesList = Grades.objects.all()
    # 将数据传递给模板，模板在渲染页面，将渲染好的页面返回浏览器
    return render(request, 'myAPP/grades.html', {"grades": gradesList})


# 查看学生表视图
from .models import Students


def students(request):
    # 去模板里取数据
    studentsList = Students.objects.all()
    # 将数据传递给模板，模板再渲染页面，将渲染好的页面返回浏览器
    return render(request, 'myAPP/students.html', {"students": studentsList})


def gradesStudents(request,num):
    grade = Grades.objects.get(pk=num)
    studentsList = grade.students_set.all()
    return render(request, 'myAPP/students.html', {"students": studentsList})
