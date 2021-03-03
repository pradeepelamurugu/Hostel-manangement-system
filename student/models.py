from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User


class Student(models.Model):

    # student = models.OneToOneField(User, on_delete=models.CASCADE)
    stu_id = models.CharField(max_length=10, null=True)
    student_name = models.CharField(max_length=200, null=True)
    father_name = models.CharField(max_length=200, null=True)
    mobile = models.IntegerField(null=True)
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    gender = models.CharField(
        choices=gender_choices,
        max_length=1,
        default=None,
        null=True)
    dob = models.DateField(
        max_length=10,
        help_text="format : YYYY-MM-DD",
        null=True)

    course = models.ForeignKey(
        'Course',
        null=True,
        default=None,
        on_delete=models.CASCADE)
    room_allotted = models.BooleanField(default=True)
    fees = models.BooleanField(default=True)

    room = models.OneToOneField(
        'Room',
        blank=True,
        on_delete=models.CASCADE,
        null=True)

    is_student = models.BooleanField(default=True)

    def __str__(self):
        return self.stu_id



class Room(models.Model):
    name = models.CharField(max_length=10,default='G1')
    room_choice = [('S', 'Single Occupancy'), ('D', 'Double Occupancy'), ('P', 'Reserved for Research Scholars'),('B', 'Both Single and Double Occupancy')]
    no = models.CharField(max_length=5)
    room_type = models.CharField(choices=room_choice, max_length=1, default=None)
    hostel = models.ForeignKey('Hostel', on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Hostel(models.Model):
    name = models.CharField(max_length=50)
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    gender = models.CharField(
        choices=gender_choices,
        max_length=1,
        default=None,
        null=True)
    caretaker = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    department_code = models.CharField(max_length=20, default=None)
    department_name = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.department_name

class Warden(models.Model):


    # warden = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    hostel = models.ForeignKey('Hostel',
        default=None,
        null=True,
        on_delete=models.CASCADE)
    is_student = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Pass(models.Model):
    applier = models.ForeignKey('Student',on_delete=models.CASCADE)
    # applier = models.CharField(max_length=200, null=True)
    fromdt = models.DateTimeField(null=True)
    todt = models.DateTimeField(null=True)
    reason_choices = [('M', 'Medical reason'), ('F', 'Family reason'),('C', 'Competitions'),('O', 'Other reason')]
    reason = models.CharField(choices=reason_choices, max_length=1, default=None)
    explaination = models.CharField(max_length=500)

    def __str__(self):
        return self.reason