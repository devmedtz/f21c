# Generated by Django 3.0.7 on 2020-09-18 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_applicationfee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='app_join',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ApplicationFee', verbose_name='Application to Join'),
        ),
    ]
