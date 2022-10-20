from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Student, Tutor


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            Tutor.objects.create(admin=instance)
        if instance.user_type == 2:
            Student.objects.create(admin=instance)

def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.tutor.save()
    if instance.user_type == 2:
        instance.student.save()