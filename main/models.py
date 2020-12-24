from django.db import models
from PIL import Image


class School(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='school_logos')

    def __str__(self):
        return self.name

class ApplicationFee(models.Model):
    APP_JOIN = (
    ('', 'Please select'),
    ('Form one', 'Form one'),
    ('Form five', 'Form five'),
    ('Transfer form one', 'Transfer form one'),
    ('Transfer form three', 'Transfer form three'),
    ('Transfer form five', 'Transfer form five'),
    )
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name='Select the school')
    form = models.CharField(max_length=100, choices=APP_JOIN, verbose_name='Application to Join')
    fee = models.DecimalField(decimal_places=0, max_digits=15, verbose_name='Application Fee')

    def __str__(self):
        return self.form

    class Meta:
        ordering = ('form',)


class DefaultLogo(models.Model):
    logo = models.ImageField(upload_to='default_logos')
        

APP_JOIN = (
    ('', 'Please select'),
    ('form one', 'Form one'),
    ('form five', 'Form five'),
    ('transfer form one', 'Transfer form one'),
    ('transfer form three', 'Transfer form three'),
    ('transfer form five', 'Transfer form five'),
)
GENDER = (
    ('', 'Please select'),
    ('male', 'Male'),
    ('female', 'Female'),
)
SPECIAL_REQUIREMENTS = (
    ('', 'Please select'),
    ('none', 'None'),
    ('Visual Impairments', 'Visual Impairments'),
    ('Hearing Impairment', 'Hearing Impairment'),
    ('Physical Impairement', 'Physical Impairement'),
    ('other', 'Other'),
)
class Student(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, verbose_name='School Name')
    app_join = models.ForeignKey(ApplicationFee, on_delete=models.SET_NULL, null=True, verbose_name='Application to Join')
    # app_join = models.CharField(max_length=100, verbose_name='Application to Join', choices=APP_JOIN)
    name = models.CharField(max_length=150, verbose_name='Student Name')
    index_no = models.CharField(max_length=150, verbose_name='Index Number', blank=True)
    parent_name = models.CharField(max_length=150, verbose_name='Parent/Guardian Name')
    form_no = models.CharField(max_length=100, verbose_name='Form Number', blank=True, null=True)
    app_date = models.DateField(verbose_name='Application Date') #should be removed
    interview_date = models.DateField(verbose_name='Interview Date', blank=True, null=True)
    passport = models.ImageField(upload_to='student_passport', verbose_name='Student Passport')
    last_school = models.CharField(max_length=200, verbose_name='Last Attended School name')
    school_contact = models.CharField(max_length=150, verbose_name='School Contacts')
    birthdate = models.DateField(verbose_name="Student's Date of Birth")
    gender = models.CharField(max_length=100, verbose_name='Student Gender', choices=GENDER)
    residence = models.CharField(max_length=200, verbose_name="Student's Place of Residence")
    parent_contact = models.CharField(max_length=200, verbose_name='Parent Contacts Details')
    payment_reference_no = models.CharField(max_length=100, verbose_name='App.Fee Payment Ref No', blank=True, null=True)
    app_id = models.CharField(max_length=100, verbose_name='Applicant ID', blank=True, null=True)
    special_requirements = models.CharField(max_length=150, verbose_name="Student's special requirements", choices=SPECIAL_REQUIREMENTS)
    f21c_contact = models.CharField(max_length=50, default='0758000090')
    paid_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    payment_status = models.BooleanField(default=False, verbose_name='Tick to mark Paid')

    def __str__(self):
        return self.name

    def save(self):
        super().save()
        passport = Image.open(self.passport.path)
        if passport.height > 130 or passport.width > 130:
            output_size = (130, 130)
            passport.thumbnail(output_size)
            passport.save(self.passport.path)

