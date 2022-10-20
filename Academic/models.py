

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class User(User):
    STUDENT = '1'
    TUTOR = '2'

    user_type_data = (TUTOR, 'TUTOR'), (STUDENT, 'STUDENT')
    user_type = models.CharField(default=1, choices=user_type_data, max_length=25)

class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete = models.CASCADE,related_name='student')
    first_name =  models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True)
    password = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.first_name

class Tutor(models.Model):
    user = models.OneToOneField(User, null=True, on_delete = models.CASCADE, related_name='tutor')
    first_name =  models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True)
    password = models.CharField(max_length=50, unique=True)
    bio = models.TextField()

    def __str__(self):
        return self.first_name


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Assignment(models.Model):
    title = models.CharField(max_length=50)
    category = models.ManyToManyField(Category, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    instructions = models.TextField()
    file = models.FileField(upload_to='images',null=True)
    image =models.ImageField(upload_to='images', blank=True)
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['-date',]


    def __str__(self):
        return self.title
 

class Answer(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=25)
    assignment = models.ForeignKey(Assignment, on_delete = models.CASCADE, null=True)
    file = models.FileField(upload_to='images', null=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)



    def __str__(self):
        return self.title