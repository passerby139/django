from django.contrib import admin

# Register your models here.
from .models import Grades, Students  # (自行引入)


# 关联创建（当创建班级表时附带要创建两个学生信息）
class StudentsInfo(admin.TabularInline):  # 也可以用admin.StackedInline
    model = Students
    extra = 2


# 注册
class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]  # 关联创建时使用
    # 列表页属性
    list_display = ['pk', 'gname', 'gdate', 'ggirlnum', 'gboynum', 'isDelete']  # 设置要显示的字段
    list_filter = ['gname']  # 设置过滤器
    search_fields = ['gname']  # 设置搜索器
    list_per_page = 5  # 设置每页显示的条数

    # 添加、修改页属性
    fields = ['ggirlnum', 'gboynum', 'gname', 'gdate', 'isDelete']  # 修改添加顺序
    '''
    fieldsets = [                                                   # 给添加的属性进行分组
        ("num", {"fields": ['ggirlnum', 'gboynum']}),
        ("base", {"fields": ['gname', 'gdate', 'isDelete']}),
    ]
    '''
    # 执行动作位置
    actions_on_top = False
    actions_on_bottom = True


admin.site.register(Grades, GradesAdmin)


# 用装饰器注册(可以删除最下面的register注册用装饰器)
# @admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    # 用于对布尔值进行判断，逻辑分析后输出
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"

    # 对于字段名进行重定义
    gender.short_description = "性别"

    # 列表页属性
    list_display = ['pk', 'sname', 'sage', gender, 'scontend', 'sgrade', 'isDelete']  # 设置要显示的字段
    list_per_page = 2  # 设置每页显示的条数

    # 添加、修改页属性
    fields = []  # 修改添加顺序
    '''
    fieldsets = []
    '''


admin.site.register(Students, StudentsAdmin)
