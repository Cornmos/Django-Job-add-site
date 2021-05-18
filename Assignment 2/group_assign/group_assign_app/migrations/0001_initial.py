# Generated by Django 3.2 on 2021-04-24 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appliedApplicants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicantFirstName', models.CharField(max_length=100)),
                ('applicantLastName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='employers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employerName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='jobAds',
            fields=[
                ('adNumber', models.IntegerField(primary_key=True, serialize=False)),
                ('jobTitle', models.CharField(max_length=100)),
                ('jobDescription', models.CharField(max_length=400)),
                ('dateAdded', models.DateTimeField(auto_now_add=True)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group_assign_app.employers')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.IntegerField(help_text='Primary Key for table', primary_key=True, serialize=False, unique=True)),
                ('emp_fname', models.CharField(help_text='First Name', max_length=100)),
                ('emp_lastname', models.CharField(help_text='Last Name', max_length=100)),
                ('emp_qualification', models.CharField(help_text='Qualification', max_length=200)),
                ('emp_expectedsalary', models.CharField(help_text='Expected Salary', max_length=100)),
                ('emp_contact_no', models.CharField(help_text='Contact number', max_length=10, unique=True)),
                ('emp_email', models.CharField(help_text='Email Address', max_length=100)),
            ],
        ),
    ]
