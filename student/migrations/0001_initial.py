# Generated by Django 3.1.7 on 2021-04-25 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_code', models.CharField(default=None, max_length=20)),
                ('department_name', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=None, max_length=1, null=True)),
                ('caretaker', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applier', models.CharField(max_length=200, null=True)),
                ('fromdt', models.DateField(max_length=10, null=True)),
                ('todt', models.DateField(max_length=10, null=True)),
                ('reason', models.CharField(choices=[('M', 'Medical reason'), ('F', 'Family reason'), ('C', 'Competitions'), ('O', 'Other reason')], default=None, max_length=1)),
                ('explaination', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='G1', max_length=10)),
                ('no', models.CharField(max_length=5)),
                ('room_type', models.CharField(choices=[('S', 'Single Occupancy'), ('D', 'Double Occupancy'), ('P', 'Reserved for Research Scholars'), ('B', 'Both Single and Double Occupancy')], default=None, max_length=1)),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.hostel')),
            ],
        ),
        migrations.CreateModel(
            name='Warden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('is_student', models.BooleanField(default=False)),
                ('hostel', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.hostel')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_id', models.CharField(max_length=10, null=True)),
                ('student_name', models.CharField(max_length=200, null=True)),
                ('father_name', models.CharField(max_length=200, null=True)),
                ('mobile', models.IntegerField(null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default=None, max_length=10, null=True)),
                ('dob', models.DateField(max_length=10, null=True)),
                ('room_allotted', models.BooleanField(default=False)),
                ('fees', models.BooleanField(default=True)),
                ('course', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.course')),
                ('room', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.room')),
            ],
        ),
    ]
