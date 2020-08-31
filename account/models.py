from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

# Create your models here.
class UserManager(BaseUserManager):

    def create_customer(self, email, password=None):
        if not email:
            raise ValueError('User must have an email address')
        #You need to set your model first
        email = self.model(email=self.normalize_email(email))
        user = self.model(email=email)
        user.set_password(password)
        #user.c_user = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_customer(
            email = email,
            password=password
        )
        user.c_user = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    objects = UserManager()
    email = models.EmailField(
        verbose_name = 'email address',
        max_length = 255,
        unique = True
    )
    active = models.BooleanField(default=True)
    c_user = models.BooleanField(default=False)


    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = [] #email password

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_cuser(self):
        return self.c_user

    @property
    def is_active(self):
        return self.active


class CustomerProfile(models.Model):
    fname = models.CharField(max_length=20)
    mname = models.CharField(max_length=20,null=True)
    lname = models.CharField(max_length=20)
    address = models.CharField(max_length=80)
    phone_no = models.IntegerField()
    cuser = models.ForeignKey(User,on_delete=models.CASCADE)

    @property
    def fullname(self):
        if self.mname == None:
            fn = self.fname + ' ' + self.lname
            return fn
        else:
            fn = self.fname + ' ' + self.mname + ' ' + self.lname
            return fn

