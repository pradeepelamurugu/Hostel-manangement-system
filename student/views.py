from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from HostelManagementSystem.settings import EMAIL_HOST_USER
from student.forms import *
from student.models import *


# Create your views here.
def home(request):
    return render(request, 'student/base.html')


def register(request):
    return render(request, 'student/register.html')


@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect(reverse('home'))


def register_student(request):
    registered = False
    if request.method == 'POST':
        var_studentForm = StudentForm(request.POST)
        if var_studentForm.is_valid():
            studentprimary = var_studentForm.save()
            studentprimary.set_password(studentprimary.password)
            studentprimary.save()
            registered = True
    else:
        var_studentForm = StudentForm()
    return render(request, 'student/register_student.html',
                  {'var_studentForm': var_studentForm, 'registered': registered})


def user_login(request):
    invalidlogin = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, f'You are now Logged in!')
                return HttpResponseRedirect(reverse('student'))
            else:
                return HttpResponse('Account not active')
        else:
            invalidlogin = True
            messages.success(request, f'Username or password incorrect')
            return redirect('user-login')
    else:
        return render(request, 'student/login.html', {'invalidlogin': invalidlogin})


def warden_login(request):
    invalidlogin = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:

                login(request, user)
                messages.success(request, f'You are now Logged in!')
                return HttpResponseRedirect(reverse('warden'))
            else:
                return HttpResponse('Account not active')
        else:
            invalidlogin = True
            messages.success(request, f'Username or password incorrect')
            return redirect('warden-login')
    else:
        return render(request, 'student/wardenlogin.html', {'invalidlogin': invalidlogin})


@login_required
def student_detail(request):
    if request.method == "POST":
        form = DetailForm(request.POST)
        if form.is_valid():
            stu = form.save(commit=False)
            stu.name = request.user
            stu.save()
            return redirect('student')
    else:
        stu = Student.objects.filter(student_name=request.user).first()
        form = DetailForm(instance=stu)
        return render(request, "student/studentdetail.html", {'form': form})

    return render(request, 'student/studentdetail.html', {'form': form})


@login_required
@staff_member_required
def warden_detail(request):
    if request.method == "POST":
        form = WardenDetailForm(request.POST)
        if form.is_valid():
            war = form.save(commit=False)
            war.name = request.user
            war.save()
            return redirect('warden')
    else:
        war = Warden.objects.filter(name=request.user).first()
        form = WardenDetailForm(instance=war)
        return render(request, "student/wardendetail.html", {'form': form})

    return render(request, 'student/wardendetail.html', {'form': form})


@login_required
def student(request):
    stu = Student.objects.filter(student_name=request.user).first()
    context = {'stude': stu}
    return render(request, 'student/student.html', context)


@login_required
@staff_member_required
def warden(request):
    war = Warden.objects.filter(name=request.user).first()
    context = {'ward': war}
    return render(request, 'student/warden.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def mentor(request):
    students = Student.objects.all()
    feepaid = Student.objects.filter(fees=True)
    feenot = Student.objects.filter(fees=False)
    pasapl = Pass.objects.all()
    roomalloted = Student.objects.filter(room_allotted=True)
    roomnotalloted = Student.objects.filter(room_allotted=False)
    passnotapproved = Pass.objects.filter(status=None)
    roomtotal = Room.objects.all()
    s = 0
    fp = 0
    fn = 0
    pa = 0
    ra = 0
    rn = 0
    pasn = 0
    rom = 0
    for i in students:
        s = s + 1
    for i in feepaid:
        fp = fp + 1
    for i in feenot:
        fn = fn + 1
    for i in pasapl:
        pa = pa + 1
    for i in roomalloted:
        ra = ra + 1
    for i in roomnotalloted:
        rn = rn + 1
    for i in passnotapproved:
        pasn = pasn + 1
    for i in roomtotal:
        rom = rom + 1

    if (rn == 0):
        rn = rom - s
    pas = pa - pasn
    d1 = {'s': s, 'fp': fp, 'fn': fn, 'pa': pa, 'ra': ra, 'rn': rn, 'pas': pas, 'pasn': pasn, 'rom': rom}
    return render(request, 'student/mentor.html', d1)


@login_required
@staff_member_required
def register_warden(request):
    registered = False
    if request.method == 'POST':
        var_wardenForm = WardenForm(request.POST)
        if var_wardenForm.is_valid():
            wardenprimary = var_wardenForm.save()
            wardenprimary.set_password(wardenprimary.password)
            wardenprimary.save()
            registered = True
    else:
        var_wardenForm = WardenForm()
    return render(request, 'student/registerWarden.html', {'var_wardenForm': var_wardenForm, 'registered': registered})


def status(request):
    room_list = Room.objects.all()
    context = {'rooms': room_list}
    return render(request, 'student/status.html', context)


@login_required
@staff_member_required
def create_room(request):
    if request.method == "POST":
        form = CreateRoomForm(request.POST)
        if form.is_valid():
            ro = form.save(commit=False)
            ro.save()
            return redirect('warden')
    else:
        form = CreateRoomForm()

    return render(request, 'student/createroom.html', {'form': form})


@login_required
@staff_member_required
def fees_status(request):
    stu_list = Student.objects.all()
    context = {'students': stu_list}
    return render(request, 'student/feesstatus.html', context)


@login_required
def pass_apply(request):
    if request.method == "POST":
        form = PassApplyForm(request.POST)
        if form.is_valid():
            pas = form.save(commit=False)
            pas.applier = request.user
            pas.save()
            return redirect('student')
    else:
        form = PassApplyForm()
    return render(request, 'student/passapply.html', {'form': form})


@login_required
@staff_member_required
def pass_decision(request):
    pass_list = Pass.objects.all()
    context = {'passes': pass_list}
    return render(request, 'student/passdecision.html', context)


@login_required
@staff_member_required
def sendmail(request):
    pas = Pass.objects.filter(applier=request.POST["appliername"]).first()
    use = User.objects.filter(username=request.POST["appliername"]).first()
    if request.method == 'POST':
        if 'accept' in request.POST["decision"]:
            pas.status = 'accpeted'
            pas.save()
        mai = use.email
        subject = 'Pass approval'
        message = 'Hello, ' + use.username + '\nYour pass was approved!!!\nThat is from ' + str(
            pas.fromdt) + 'to ' + str(pas.todt) + '.\nThank you \nregards\n-' + request.user.email + '.'
        recepient = mai
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
        messages.success(request, f'Mail has been sent!')

        return render(request, 'student/mailsent.html', {'recepient': recepient})
    return render(request, 'student/passdecision.html')


@user_passes_test(lambda u: u.is_superuser)
def students_list(request):
    stu = Student.objects.all()
    context = {'students': stu}
    return render(request, 'student/students_list.html', context)


@user_passes_test(lambda u: u.is_superuser)
def warden_list(request):
    war = Warden.objects.all()
    context = {'ward': war}
    return render(request, 'student/warden_list.html', context)


@user_passes_test(lambda u: u.is_superuser)
def hostel_list(request):
    host = Hostel.objects.all()
    context = {'hostels': host}
    return render(request, 'student/hostel_list.html', context)


@user_passes_test(lambda u: u.is_superuser)
def pass_list(request):
    pas = Pass.objects.all()
    context = {'passes': pas}
    return render(request, 'student/pass_list.html', context)


def hostel_detail_view(request, hostel_name):
    try:
        this_hostel = Hostel.objects.get(name=hostel_name)
    except Hostel.DoesNotExist:
        raise Http404("Invalid Hostel Name")
    context = {
        'hostel': this_hostel,
        'rooms': Room.objects.filter(
            hostel=this_hostel)
    }
    return render(request, 'student/hostel_detail_view.html', context)


def about(request):
    return render(request, 'student/about.html')


def mentor_login(request):
    invalidlogin = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, f'You are now Logged in!')
                return HttpResponseRedirect(reverse('mentor'))
            else:
                return HttpResponse('Account not active')
        else:
            invalidlogin = True
            messages.success(request, f'Your username or password is incorrect!')
            return redirect('mentor-login')
    else:
        return render(request, 'student/mentorlogin.html', {'invalidlogin': invalidlogin})


def hostel_detail_list(request):
    host = Hostel.objects.all()
    context = {'hos': host}
    return render(request, 'student/hostel_detail_list.html', context)


@transaction.atomic
def select_room(request):
    if request.method == 'POST':
        form = SelectRoomForm(request.POST)
        if form.is_valid():
            stu = Student.objects.filter(student_name=request.user).first()
            rom = Room.objects.filter(name=form.cleaned_data.get("room")).first()
            stu.room = rom
            stu.room_allotted = True
            stu.save()
            return redirect('student')
    else:
        form = SelectRoomForm()
    return render(request, 'student/selectroom.html', {'form': form})
