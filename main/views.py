from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .forms import StudentForm
from .models import School, DefaultLogo

from django.views.generic import View  # pdf download
from django.template.loader import get_template
from .utils import render_to_pdf  #created in step 4
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .models import Student, ApplicationFee

def load_logos(request):
    school_id = request.GET.get('school')
    if school_id == '':
        schools = DefaultLogo.objects.get(id=1)
    else:
        schools = School.objects.get(id=school_id)
    
    return render(request, 'main/logo.html', {'schools': schools})

def load_fee(request):
    school_id = request.GET.get('school')
    app_id = request.GET.get('form_id')

    print('app_id', app_id)
    print('school_id', school_id)


    
    fee = ApplicationFee.objects.get(school_id=school_id, id=app_id)

    print('fee', fee)

    return render(request, 'main/fee.html', {'fee':fee})

def load_forms(request):
    school_id = request.GET.get('school')
    forms = ApplicationFee.objects.filter(school_id=school_id)
    return render(request, 'main/form_dropdown_list_options.html', {'forms': forms})


class StudentFormView(FormView):
    form_class = StudentForm
    template_name = 'main/index.html'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if request.method == 'POST':
            if form.is_valid():
                student = form.save(commit=False)
                form.save()

                # show the pdf form download link
                student_id = urlsafe_base64_encode(force_bytes(student.id))
                print('student_id:', student_id)
                url = 'http://application.f21c.co.tz' + reverse('main:pdf', kwargs={'student_id': student_id})

                return redirect(reverse('main:success', kwargs={'student_id': student_id}))
            else:
                return self.form_invalid(form)


def success(request, student_id):
    url = 'http://application.f21c.co.tz' + reverse('main:pdf', kwargs={'student_id': student_id})

    context = {
        'url':url,
    }
    return render(request, 'main/success.html', context)


class GeneratePdf(View):
    def get(self, request, student_id):

        id = force_text(urlsafe_base64_decode(student_id))
        
        students = Student.objects.get(id=id)

        data = {
            'application_date': students.created.date, 
            'school_name': students.school.name.upper(),
            'school_logo' : students.school.logo,
            'app_join': students.app_join,
            'student_name': students.name.upper(),
            'index_no':students.index_no,
            'parent_name':students.parent_name,
            'form_no':students.form_no,
            'interview_date':students.interview_date,
            'passport':students.passport,
            'last_school':students.last_school,
            'school_contact':students.school_contact,
            'birthdate':students.birthdate,
            'gender':students.gender.upper(),
            'residence':students.residence,
            'parent_contact':students.parent_contact,
            'payment_reference_no':students.payment_reference_no,
            'app_id':students.app_id,
            'special_requirements':students.special_requirements,
            'f21c_contact':students.f21c_contact, 
        }
        pdf = render_to_pdf('main/pdf_template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

