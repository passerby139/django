from django.db import models


# Create your models here.

class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField()

    def __str__(self):
        return self.gname


class StudentsManager(models.Manager):
    def get_queryset(self):
        return super(StudentsManager, self).get_queryset().filter(isDelete=False)


class Students(models.Model):
    # 自定义模型管理器后，object就不存在了
    stuObj = models.Manager()
    stuObj2 = StudentsManager()
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=False)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    sgrade = models.ForeignKey("Grades", on_delete=models.CASCADE)  # 定义外键的时候必须定义级联删除
    # 定义一个类方法创建对象
    @classmethod
    def createStudent(cls,name,age,gender,contend,grade,isD=False):
        stu = cls(sname=name,sage=age,sgender=gender,scontend=contend,sgrade=grade,isDelete=isD)
        return stu
