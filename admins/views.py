import csv
from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, CreateView, ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from main.models import Student, School, ApplicationFee
from datetime import datetime, timedelta, date
from .forms import SchoolForm, ApplicationFeeForm
from django.urls import reverse_lazy

from django.views.generic import View  # pdf download
from django.template.loader import get_template
from main.utils import render_to_pdf  #created in step 4
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode



class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'admins/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        one_week_ago = datetime.today() - timedelta(days=7)
        context['students'] = Student.objects.all().order_by('-created')
        context['schools'] = School.objects.all()
        context['today_student'] = Student.objects.filter(created__date=datetime.today())
        context['week_student'] = Student.objects.filter(created__gte=one_week_ago)
        return context


class SchoolCreate(LoginRequiredMixin, CreateView):
    form_class = SchoolForm
    template_name = 'admins/school_add.html'
    success_url = reverse_lazy('admins:schools')


class SchoolUpdateView(LoginRequiredMixin, UpdateView):
    model = School
    fields = '__all__'
    template_name = 'admins/school_update.html'
    success_url = reverse_lazy('admins:schools')


class SchoolDeleteView(LoginRequiredMixin, DeleteView):
    model = School
    success_url = reverse_lazy('admins:schools')


class ApplicationFeeView(LoginRequiredMixin, CreateView):
    form_class = ApplicationFeeForm
    template_name = 'admins/app_fee.html'
    success_url = reverse_lazy('admins:app-fee-list')
    

class ApplicationFeeListView(LoginRequiredMixin, ListView):
    model = ApplicationFee
    template_name = 'admins/app_fee_list.html'
    context_object_name = 'fees'
    ordering = ['-school__name']

class ApplicationFeeUpdate(LoginRequiredMixin, UpdateView):
    model = ApplicationFee
    fields = '__all__'
    template_name = 'admins/app_fee_update.html'
    success_url = reverse_lazy('admins:app-fee-list')


class ApplicationFeeDelete(LoginRequiredMixin, DeleteView):
    model = ApplicationFee
    success_url = reverse_lazy('admins:app-fee-list')



class SchoolListView(LoginRequiredMixin, ListView):
    model = School
    template_name = 'admins/schools.html'
    context_object_name = 'schools'


class StudentsListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'admins/students.html'
    context_object_name = 'students'
    ordering = ['-created']


class StudentUpdate(LoginRequiredMixin, UpdateView):
    model = Student
    fields = ['school','name','index_no','parent_name','form_no','app_id','app_date','passport','last_school','school_contact','birthdate','gender','residence','parent_contact','special_requirements','f21c_contact','interview_date','payment_reference_no','paid_amount','transaction_id','payment_status']
    template_name = 'admins/student_update.html'
    success_url = reverse_lazy('admins:students')


class GeneratePdfViews(LoginRequiredMixin, View):
    def get(self, request, id):
        
        students = Student.objects.get(id=id)

        data = {
            'date': students.created, 
            'school_name': students.school.name,
            'school_logo' : students.school.logo,
            'app_join': students.app_join,
            'student_name': students.name,
            'index_no':students.index_no,
            'parent_name':students.parent_name,
            'form_no':students.form_no,
            'interview_date':students.interview_date,
            'passport':students.passport,
            'last_school':students.last_school,
            'school_contact':students.school_contact,
            'birthdate':students.birthdate,
            'gender':students.gender,
            'residence':students.residence,
            'parent_contact':students.parent_contact,
            'payment_reference_no':students.payment_reference_no,
            'app_id':students.app_id,
            'special_requirements':students.special_requirements,
            'f21c_contact':students.f21c_contact, 
        }
        pdf = render_to_pdf('main/form_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('admins:students')


class ExportStudentsCsv(LoginRequiredMixin, View):

    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="students-applications.csv"'

        writer = csv.writer(response)
        writer.writerow(['school','app_join','name','index_no','parent_name','form_no','app_id','app_date','passport','last_school','school_contact','birthdate','gender','residence','parent_contact','special_requirements','f21c_contact','interview_date','payment_reference_no','paid_amount','transaction_id','payment_status'])

        students = Student.objects.all().values_list('school__name','app_join','name','index_no','parent_name','form_no','app_id','app_date','passport','last_school','school_contact','birthdate','gender','residence','parent_contact','special_requirements','f21c_contact','interview_date','payment_reference_no','paid_amount','transaction_id','payment_status')
        for student in students:
            writer.writerow(student) 

        return response