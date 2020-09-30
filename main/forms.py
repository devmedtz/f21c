from django import forms

from .models import School, Student, ApplicationFee


class StudentForm(forms.ModelForm):
    school = forms.ModelChoiceField(School.objects.all(), empty_label='Please select', label='School Name')

    class Meta:
        model = Student
        exclude = ['created', 'modified', 'form_no', 'interview_date', 'payment_reference_no', 'app_id', 'f21c_contact', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['app_join'].queryset = ApplicationFee.objects.none()

        if 'school' in self.data:
            try:
                school_id = int(self.data.get('school'))
                self.fields['app_join'].queryset = ApplicationFee.objects.filter(school_id=school_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['app_join'].queryset = self.instance.school.app_join_set

