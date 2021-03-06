# Generated by Django 3.0.7 on 2020-09-18 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200918_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='app_join',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.ApplicationFee', verbose_name='Application to Join'),
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.School', verbose_name='School Name'),
        ),
    ]
