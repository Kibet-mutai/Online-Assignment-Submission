from django.urls import path, include

from . import views





urlpatterns = [
    path('', views.Home, name = 'home'),
    path('staff_home', views.Home, name = 'Staff_home'),
    path('list', views.list_assignment, name='assignment_list'),
    path('detail/<int:id>/', views.assignment_detail, name='assignment_details'),
    path('create', views.create_assignment, name='create'),
    path('update/<int:id>/', views.update_assignment, name='update'),
    path('delete/<int:id>/', views.delete_assignment, name='delete'),
    path('login', views.student_login, name='login'),
    path('register', views.register_student, name='register'),
    path('register_tutor', views.register_tutor, name='register_tutor'),
    path('logout', views.logout_page, name='logout'),
    path('user', views.user_page, name='user_profile'),
    path('delete_answer/<int:id>/', views.delete_answer, name='delete_answer'),
    path('update_answer/<int:id>/', views.update_answer, name='update_answer'),
    path('create_answer/<int:id>/', views.create_answer, name='create_answer'),
]

