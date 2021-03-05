from django import forms
from django.contrib.auth.models import User
from student.models import *

class studentForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(help_text=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=['first_name','username','email','password']

    def clean(self):
        cleaned_data = super(studentForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")


        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
class wardenForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(help_text=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=['first_name','username','email','password']

class detailform(forms.ModelForm):
    student_name = forms.CharField(help_text='Same as you registered name')
    class Meta:
        model = Student
        fields = ('stu_id', 'student_name','father_name','mobile',
                  'gender','dob','course','fees')

class wardendetailform(forms.ModelForm):
    class Meta:
        model = Warden
        fields = ('name','hostel')

class createroomform(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('name','no','room_type','hostel')

class passapplyform(forms.ModelForm):
    class Meta:
        model = Pass
        fields = ('fromdt','todt','reason','explaination')

class selectroomform(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('room',)
