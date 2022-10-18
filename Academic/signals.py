from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Student, Tutor


def student_profile(sender, instance, created, **kwargs):
     if created:
        group = Group.objects.get(name='student')
        instance.groups.add(group)

        Student.objects.create(
            user=instance,
            name=instance.username,
        )
        print('Profile created!')
post_save.connect(student_profile, sender=User)


def tutor_profile(sender, instance, created, **kwargs):
     if created:
        group = Group.objects.get(name='tutor')
        instance.groups.add(group)

        Tutor.objects.create(
            user=instance,
            name=instance.username,
        )
        print('Profile created!')
post_save.connect(tutor_profile, sender=User)
