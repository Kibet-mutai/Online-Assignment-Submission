# Generated by Django 4.1.1 on 2022-10-11 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Academic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='category',
            field=models.ManyToManyField(null=True, to='Academic.category'),
        ),
        migrations.AddField(
            model_name='order',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Academic.student'),
        ),
    ]
