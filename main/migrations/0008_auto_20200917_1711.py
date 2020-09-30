# Generated by Django 3.0.7 on 2020-09-17 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200916_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='special_requirements',
            field=models.CharField(choices=[('', 'Please select'), ('none', 'None'), ('Visual Impairments', 'Visual Impairments'), ('Hearing Impairment', 'Hearing Impairment'), ('Physical Impairement', 'Physical Impairement'), ('other', 'Other')], max_length=150, verbose_name="Student's special requirements"),
        ),
    ]
