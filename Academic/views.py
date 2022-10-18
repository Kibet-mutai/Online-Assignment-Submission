from multiprocessing import context
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import logout, login, authenticate
from Academic.forms import AnswerForm, AssignmentForm, createUSerForm
from django.contrib import messages
from Academic.models import Answer, Assignment, Student, Tutor
from .decorators import admin, allowed_user, unauthenticated_user
from django.utils.decorators import method_decorator


# Create your views here.

def Home(request):
    return render(request, 'Academic/index.html')

@allowed_user(allowed_roles=['staff'])
def student_home(request):
    return render(request, 'Academic/student_home.html')

@login_required(login_url='login')
@admin
def student(request, id):
    students = Student.objects.get(id=id)
    assignments = students.order_set.all()
    assignments_count = assignments.count()
    
    context = {'students':students, 'assignments':assignments, 'assignments_count':assignments_count}
    return render(request, 'Academic/student.html', context)

# @login_required(login_url='login')
# @allowed_user(allowed_roles=['student'])
def user_page(request):
    assignments = request.user.student.assignment_set(all)
    print('assignments:', assignments)
    context = {'assignments':assignments}
    return render(request, 'Academic/user.html', context)

# @allowed_user(allowed_roles=['admin','staff'])
@login_required(login_url='login')
def list_assignment(request):
    if request.method == 'GET':
    
        assignments = Assignment.objects.all()
        form = AssignmentForm(assignments)
        context = {'assignments':assignments}
        return render(request, 'Academic/list.html', context)
    

# every detail of the order
@login_required(login_url='login')
def assignment_detail(request,id):
    try:
        assignments = Assignment.objects.get(id=id)
        context = {'assignments':assignments}
        return render(request, 'Academic/detail.html', context)
    except Assignment.DoesNotExist:
        return redirect('home')



#creating order
@login_required(login_url='login')
def create_assignment(request):
    form = AssignmentForm()
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        
        if form.is_valid:
            form.save(commit=False)
            return redirect('order_detail')
    context = {'form':form}
    return render(request, 'order_list', context)
    

#updating order
@login_required(login_url='login')
def update_assignment(request, id):
    assignments = Assignment.objects.get(id=id)
    form = AssignmentForm(instance=assignments)

    if request.method == 'PUT':
        form = AssignmentForm(request.PUT,request.FILES, instance=assignments)
        if form.is_valid():
            form.save()
            return redirect('order_detail')

    context = {'form':form}
    return render(request, 'Academic/detail.html', context)


@login_required(login_url='login')
def delete_assignment(request,id):
    assignments = Assignment.objects.get(id=id)

    if request.method == 'POST':
        assignments.delete()
        return redirect('assignment_detail')
    context = {'items':assignments}
    return render(request, 'Academic/delete.html', context)

@login_required(login_url='login')
def create_answer(request, id):
    assignments = Assignment.objects.get(id=id)
    form = AnswerForm(instance=assignments)

    if request.method == 'POST':
        form = AnswerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            return redirect('assignment_detail')
        
        context = {'assignments':assignments, 'form':form}
        return render(request, 'Academic/answer.html', context)

@login_required(login_url='login')
def update_answer(request, id):
    answers = Answer.objects.get(id=id)
    form = AnswerForm(instance=answers)

    if request.method == 'PUT':
        form = AnswerForm(request.PUT,request.FILES, instance=answers)
        if form.is_valid():
            form.save()
            return redirect('assignment_detail')

    context = {'form':form}
    return render(request, 'Academic/detail.html', context)



@login_required(login_url='login')
def delete_answer(request, id):
    answer = Answer.objects.get(id=id)

    if request.method == 'POST':
        answer.delete()
        return redirect('assignment_detail')
    context = {'items':answer}
    return render(request, 'Academic/delete_answer.html', context)


def answer_list(request):
    if request.method == 'GET':
    
        answers = Answer.objects.all()
        form = AssignmentForm(answers)
        context = {'assignments':answers}
        return render(request, 'Academic/answer_list.html', context)

#login user
@unauthenticated_user
def student_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password ')
        user_login = User.objects.get(username=username)
        user = authenticate(request, username = username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect!')
    
    context = {}
    return render(request, 'Academic/login.html', context)



def logout_page(request):
    logout(request)
    return redirect('home')



#register user
@unauthenticated_user
def register_student(request):
    form = createUSerForm()
    if request.method == 'POST':
        form = createUSerForm(request.POST)
        if form.is_valid():
            user = form.save() 
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully!')
            return redirect('student_login')
       
    context = {'form':form}
    return render(request, 'Academic/register.html', context)




@unauthenticated_user
def register_tutor(request):
    form = createUSerForm()
    if request.method == 'POST':
        form = createUSerForm(request.POST)
        if form.is_valid():
            user = form.save() 
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully!')
            return redirect('tutor_login')
       
    context = {'form':form}
    return render(request, 'Academic/register.html', context)


@unauthenticated_user
def tutor_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password ')
        user_login = User.objects.get(username=username)
        user = authenticate(request, username = username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect!')
    
    context = {}
    return render(request, 'Academic/tutor_login.html', context)

