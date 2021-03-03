from django.contrib import admin
from student.models import *

admin.site.register(Student)
admin.site.register(Room)
admin.site.register(Hostel)
admin.site.register(Course)
admin.site.register(Warden)
admin.site.register(Pass)