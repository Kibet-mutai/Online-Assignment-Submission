from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import logout, login, authenticate
from Academic.forms import AnswerForm, AssignmentForm, SignupForm, LoginForm
from django.contrib import messages
from Academic.models import Answer, Assignment, User, Student, Tutor
from django.utils.decorators import method_decorator


# Create your views here.

def Home(request):
    return render(request, 'Academic/index.html')

def student_home(request):
    return render(request, 'Academic/student_home.html')

def tutor_home(request):
    return render(request, 'Academic/tutor_home.html')

@login_required(login_url='login')

def student(request, id):
    students = Student.objects.get(id=id)
    assignments = students.assignmnent_set.all()
    assignments_count = assignments.count()
    
    context = {'students':students, 'assignments':assignments, 'assignments_count':assignments_count}
    return render(request, 'Academic/student.html', context)


def user_page(request):
    assignments = request.user.student.assignment_set(all)
    print('assignments:', assignments)
    context = {'assignments':assignments}
    return render(request, 'Academic/user.html', context)


@login_required(login_url='login')
def list_assignment(request):
    if request.method == 'GET':
    
        assignments = Assignment.objects.all()
        form = AssignmentForm(assignments)
        context = {'assignments':assignments}
        return render(request, 'Academic/list.html', context)
    


@login_required(login_url='login')
def assignment_detail(request,id):
    try:
        assignments = Assignment.objects.get(id=id)
        context = {'assignments':assignments}
        return render(request, 'Academic/detail.html', context)
    except Assignment.DoesNotExist:
        return redirect('assignment_list')


@login_required(login_url='login')
def create_assignment(request):
    form = AssignmentForm()
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        
        if form.is_valid:
            form.save(commit=False)
            return redirect('assignment_detail')
    context = {'form':form}
    return render(request, 'Academic/assignment_form.html', context)
    


@login_required(login_url='login')
def update_assignment(request, id):
    assignments = Assignment.objects.get(id=id)
    form = AssignmentForm(instance=assignments)

    if request.method == 'PUT':
        form = AssignmentForm(request.PUT,request.FILES, instance=assignments)
        if form.is_valid():
            form.save()
            return redirect('assignment_detail')

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
def create_answer(request):
    form = AnswerForm()
    if request.method == 'POST':
        form = AnswerForm(request.POST, request.FILES)
        
        if form.is_valid:
            form.save(commit=False)
            return redirect('assignment_detail')
    context = {'form':form}
    return render(request, 'Academic/answer_form.html', context)

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
    return render(request, 'Academic/answer_form.html', context)



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
    

@login_required(login_url='login')
def answer_detail(request,id):
    try:
        answers = Answer.objects.get(id=id)
        context = {'assignments':answers}
        return render(request, 'Academic/answer_detail.html', context)
    except Answer.DoesNotExist:
        return redirect('answer_list')



def SignUp(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save() 
            
            messages.success(request, 'Account created successfully!')
            return redirect('login')
        else:
            messages.error(request, 'Form is not valid!')
       
    context = {'form':form}
    return render(request, 'Academic/register.html', context)



def login_page(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password ')
            user = authenticate(request, username=username, password=password)
        if user is not None and user.is_tutor:
            login(request, user)
            return redirect('tutor_home') 
        if user is not None and user.is_student:
            login(request, user)
            print('Login!')
            return redirect('student_home') 
        else:
            messages.info(request, 'Username OR Password is incorrect!')
    context = {'form':form}
    return render(request, 'Academic/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('home')