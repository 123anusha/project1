from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='sin'),
    path('csignup/',views.c_signup,name='csup'),
    path('logout/',views.logout,name='sut'),
]