# Generated by Django 3.0.7 on 2020-12-24 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20200918_1218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applicationfee',
            options={'ordering': ('form',)},
        ),
        migrations.AlterField(
            model_name='applicationfee',
            name='form',
            field=models.CharField(choices=[('', 'Please select'), ('Form one', 'Form one'), ('form five', 'Form five'), ('transfer form one', 'Transfer form one'), ('transfer form three', 'Transfer form three'), ('transfer form five', 'Transfer form five')], max_length=100, verbose_name='Application to Join'),
        ),
    ]
