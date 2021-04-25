from django.urls import path

from student import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('registerStudent/', views.register_student, name='register-student'),
    path('logout/', views.user_logout, name='logout'),
    path('login_student/', views.user_login, name='user-login'),
    path('login_warden/', views.warden_login, name='warden-login'),
    path('student/', views.student, name='student'),
    path('warden/', views.warden, name='warden'),
    path('mentor/', views.mentor, name='mentor'),
    path('details/', views.student_detail, name='detail'),
    path('wardendetails/', views.warden_detail, name='warden-detail'),
    path('registerWarden/', views.register_warden, name='register-warden'),
    # path('hostels/<slug:hostel_name>/', views.hostel_detail_view, name='hostel'),
    path('status/', views.status, name='status'),
    path('createroom/', views.create_room, name='create-room'),
    # path('dashboard', views.dashboard, name='dashboard'),
    path('feesstatus/', views.fees_status, name='fees-status'),
    path('passapply/', views.pass_apply, name='pass-apply'),
    path('passdecision/', views.pass_decision, name='pass-decision'),
    path('sendmail/', views.sendmail, name='send-mail'),
    path('students_list/', views.students_list, name='students-list'),
    path('warden_list/', views.warden_list, name='warden-list'),
    path('hostel_list/', views.hostel_list, name='hostel-list'),
    path('pas_list/', views.pass_list, name='pass-list'),
    path('hostel_detail_list/hostels/<slug:hostel_name>/', views.hostel_detail_view, name='hostel-detail-view'),
    path('about/', views.about, name='about'),
    path('login_mentor/', views.mentor_login, name='mentor-login'),
    path('hostel_detail_list/', views.hostel_detail_list, name='hostel-detail-list'),
    path('selectroom/', views.select_room, name='select-room'),

]
