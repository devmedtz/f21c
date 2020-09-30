from django import forms
from main.models import School, ApplicationFee


class SchoolForm(forms.ModelForm):

    class Meta:
        model = School
        fields = '__all__'


class ApplicationFeeForm(forms.ModelForm):

    class Meta:
        model = ApplicationFee
        fields = '__all__'
