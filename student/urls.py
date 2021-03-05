from django.urls import path
from student import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.register,name='register'),
    path('registerStudent/', views.registerStudent, name='registerStudent'),
    path('logout/', views.userLogout, name='logout'),
    path('login_student/',views.userLogin,name='userLogin'),
    path('login_warden/',views.wardenLogin,name='wardenLogin'),
    path('student/',views.student,name='student'),
    path('warden/',views.warden,name='warden'),
    path('mentor/',views.mentor,name='mentor'),
    path('details/', views.student_detail, name='detail'),
    path('wardendetails/', views.warden_detail, name='wardendetail'),
    path('registerWarden/',views.registerWarden,name='registerWarden'),
    # path('hostels/<slug:hostel_name>/', views.hostel_detail_view, name='hostel'),
    path('status/',views.status,name='status'),
    path('createroom/',views.createroom,name='createroom'),
    # path('dashboard', views.dashboard, name='dashboard'),
    path('feesstatus/',views.feesstatus,name='feesstatus'),
    path('passapply/',views.passapply,name='passapply'),
    path('passdecision/',views.passdecision,name='passdecision'),
    path('sendmail/',views.sendmail,name='sendmail'),
    path('students_list/',views.students_list,name='students_list'),
path('warden_list/',views.warden_list,name='warden_list'),
path('hostel_list/',views.hostel_list,name='hostel_list'),
path('pas_list/',views.pass_list,name='pass_list'),
path('hostel_detail_list/hostels/<slug:hostel_name>/', views.hostel_detail_view, name='hostel_detail_view'),
path('about/',views.about,name='about'),
path('login_mentor/',views.mentorLogin,name='mentorLogin'),
path('hostel_detail_list/',views.hostel_detail_list,name='hostel_detail_list'),
path('selectroom/',views.selectroom,name='selectroom'),






]