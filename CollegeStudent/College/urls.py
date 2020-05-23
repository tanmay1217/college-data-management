from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('college/',views.college,name='college'),
    path('student/',views.student,name='student'),
    path('college/<int:id>',views.college_student,name='college_student'),
    path('addcollege/',views.addcollege,name='addcollege'),
    path('addstudent/',views.addstudent,name='addstudent'),
    path('admin/doc',include('django.contrib.admindocs.urls')),
]
