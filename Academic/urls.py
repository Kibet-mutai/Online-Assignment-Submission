from django.urls import path, include

from . import views





urlpatterns = [
    path('', views.Home, name = 'home'),
    path('student_home', views.student_home, name = 'student_home'),
    path('tutor_home', views.tutor_home, name = 'tutor_home'),
    path('list', views.list_assignment, name='assignment_list'),
    path('detail/<int:id>/', views.assignment_detail, name='assignment_details'),
    path('create', views.create_assignment, name='create'),
    path('update/<int:id>/', views.update_assignment, name='update'),
    path('delete/<int:id>/', views.delete_assignment, name='delete'),
    path('register', views.SignUp, name='register'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
    path('user', views.user_page, name='user_profile'),
    path('delete_answer/<int:id>/', views.delete_answer, name='delete_answer'),
    path('update_answer/<int:id>/', views.update_answer, name='update_answer'),
    path('create_answer', views.create_answer, name='create_answer'),
    path('answer_list', views.answer_list, name='answer_list'),
    path('answer_detail/<int:id>/', views.answer_detail, name='answer_detail'),
]

