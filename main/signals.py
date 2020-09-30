from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student


@receiver(post_save, sender=Student)
def student_form_no(sender, instance, created, **kwargs):
    if created:
        a = instance.school.name
        a = a[:2].upper()
        form_no = a + str(instance.id) + "F21C" + str(instance.created.hour) + str(instance.created.minute) + str(instance.created.year)[-2:] + str(instance.name)[:2].upper()
        app_id = str(instance.parent_contact)[-3:] + str(instance.birthdate.day) + str(instance.birthdate.month) + str(instance.birthdate.year)[-3:]
        Student.objects.filter(pk=instance.pk).update(form_no=form_no)
        Student.objects.filter(pk=instance.pk).update(app_id=app_id)
        print("Application id:", app_id)