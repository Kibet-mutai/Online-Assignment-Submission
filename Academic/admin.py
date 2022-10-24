from django.contrib import admin

from Academic.models import Answer, Category, Student, Tutor, Assignment,User

# Register your models here.
admin.site.register(User)
admin.site.register(Assignment)
admin.site.register(Student)
admin.site.register(Category)
admin.site.register(Tutor)
admin.site.register(Answer)