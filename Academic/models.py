

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User, AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin = models.BooleanField('is_admin', default=False)
    is_student = models.BooleanField('is_student', default=False)
    is_tutor = models.BooleanField('is_tutor', default=False)

class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete = models.CASCADE)
    first_name =  models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True)

    def __str__(self):
        return self.first_name

class Tutor(models.Model):
    user = models.OneToOneField(User, null=True, on_delete = models.CASCADE)
    first_name =  models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True)
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