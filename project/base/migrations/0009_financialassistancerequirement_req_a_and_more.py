# Generated by Django 4.2.7 on 2023-11-26 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_remove_financialassistancerequirement_req_a_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialassistancerequirement',
            name='req_a',
            field=models.CharField(default='False', max_length=100),
        ),
        migrations.AddField(
            model_name='financialassistancerequirement',
            name='req_b',
            field=models.CharField(default='False', max_length=100),
        ),
        migrations.AddField(
            model_name='financialassistancerequirement',
            name='req_c',
            field=models.CharField(default='False', max_length=100),
        ),
        migrations.AddField(
            model_name='financialassistancerequirement',
            name='req_d',
            field=models.CharField(default='False', max_length=100),
        ),
        migrations.AddField(
            model_name='financialassistancerequirement',
            name='req_e',
            field=models.CharField(default='False', max_length=100),
        ),
        migrations.AddField(
            model_name='financialassistancerequirement',
            name='req_f',
            field=models.CharField(default='False', max_length=100),
        ),
        migrations.AddField(
            model_name='financialassistancerequirement',
            name='req_g',
            field=models.CharField(default='False', max_length=100),
        ),
        migrations.AddField(
            model_name='financialassistancerequirement',
            name='req_h',
            field=models.CharField(default='False', max_length=100),
        ),
    ]
