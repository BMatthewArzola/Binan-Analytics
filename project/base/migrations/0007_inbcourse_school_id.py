# Generated by Django 4.2.5 on 2023-11-30 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_inbcourse_school_inbcourse_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='inbcourse',
            name='school_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
