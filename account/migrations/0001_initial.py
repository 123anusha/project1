# Generated by Django 3.0.1 on 2020-02-04 07:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('active', models.BooleanField(default=True)),
                ('s_user', models.BooleanField(default=False)),
                ('c_user', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('w_user', models.BooleanField(default=False)),
                ('m_user', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('mname', models.CharField(max_length=20, null=True)),
                ('lname', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=80)),
                ('phone_no', models.IntegerField()),
                ('wuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SupplierProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('mname', models.CharField(max_length=20, null=True)),
                ('lname', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=80)),
                ('phone_no', models.IntegerField()),
                ('business_name', models.CharField(max_length=50)),
                ('suser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ManagerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('mname', models.CharField(max_length=20, null=True)),
                ('lname', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=80)),
                ('phone_no', models.IntegerField()),
                ('muser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('mname', models.CharField(max_length=20, null=True)),
                ('lname', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=80)),
                ('phone_no', models.IntegerField()),
                ('cuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
