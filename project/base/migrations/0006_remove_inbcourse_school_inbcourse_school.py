# Generated by Django 4.2.5 on 2023-11-30 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_inbcourse_school_inbcourse_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inbcourse',
            name='school',
        ),
        migrations.AddField(
            model_name='inbcourse',
            name='school',
            field=models.ManyToManyField(to='base.inbschool'),
        ),
    ]