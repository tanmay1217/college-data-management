from django import forms
from .models import College,Student

class CollegeForm(forms.ModelForm):
    class Meta:
        model=College
        fields="__all__"

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
