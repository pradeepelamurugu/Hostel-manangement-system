from django import forms
from django.contrib.auth.models import User

from student.models import *


class StudentForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            # 'confirm_password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            "first_name": "First Name",
            "username": "Username",
            "email": "Email",
            "password": "Password",
            "confirm_password": "Confirm Password",

        }

    def clean(self):
        cleaned_data = super(StudentForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class WardenForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            "first_name": "First Name",
            "username": "Username",
            "email": "Email",
            "password": "Password",
            "confirm_password": "Confirm Password",

        }


class DetailForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('stu_id', 'student_name', 'father_name', 'mobile',
                  'gender', 'dob', 'course', 'fees')

        widgets = {
            'stu_id': forms.TextInput(attrs={'class': 'form-control'}),
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'dob': forms.SelectDateWidget(attrs={'class': 'form-control'}, years=range(1900, 2020)),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'fees': forms.CheckboxInput(attrs={'class': 'form-control'}),

        }
        labels = {
            "stu_id": "Roll Number",
            "student_name": "Student Name",
            "father_name": "Father Name",
            "mobile": "Phone Number",
            "dob": "Date of Birth",
            "course": "Course",
            "fees": "Fees",
            "gender": "Gender",

        }


class WardenDetailForm(forms.ModelForm):
    class Meta:
        model = Warden
        fields = ('name', 'hostel')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'hostel': forms.Select(attrs={'class': 'form-control'}),

        }
        labels = {
            "name": "Name",
            "hostel": "Hostel",
        }


class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('name', 'no', 'room_type', 'hostel')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'no': forms.TextInput(attrs={'class': 'form-control'}),
            'room_type': forms.Select(attrs={'class': 'form-control'}),
            'hostel': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            "name": "Name",
            "no": "Room Number",
            "room_type": "Room Type",
            "hostel": "Hostel",

        }


class PassApplyForm(forms.ModelForm):
    class Meta:
        model = Pass
        fields = ('fromdt', 'todt', 'reason', 'explaination')

        widgets = {
            'fromdt': forms.SelectDateWidget(attrs={'class': 'form-control'}, years=range(1900, 2022)),
            'todt': forms.SelectDateWidget(attrs={'class': 'form-control'}, years=range(1900, 2022)),
            'reason': forms.Select(attrs={'class': 'form-control'}),
            'explaination': forms.Textarea(attrs={'class': 'form-control'}),

        }
        labels = {
            "fromdt": "From Date and Time",
            "todt": "To Date and Time",
            "reason": "Reason",
            "explaination": "Explaination",
        }


class SelectRoomForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('room',)

        widgets = {

            'room': forms.Select(attrs={'class': 'form-control'}),

        }
        labels = {

            "room": "Select Room",

        }
