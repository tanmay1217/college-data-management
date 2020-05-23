from django.shortcuts import render,redirect
from .models import College,Student
from django.http import HttpResponse
from .forms import CollegeForm,StudentForm

def home(request):
    college = College.objects.all()
    student = Student.objects.all()
    return render(request,'college/home.html',{'C':college,'S':student})
def college(request):
    college = College.objects.all()
    return render(request,'college/collge.html',{'C':college,'title':'College'})
def student(request):
    student = Student.objects.all()
    return render(request,'college/student.html',{'S':student,'title':'Student'})
def college_student(request,id):
    collegedata = College.objects.get(id =id)
    #print(collegedata) SKIT
    studentdata = Student.objects.filter(college = collegedata)
    #print(studentdata) [<Student: aaa>, <Student: a1>]>
    return render(request,'college/studentdata.html',{'S':studentdata ,'title':'CollegeDetails'})
def addcollege(request):
    form =CollegeForm()
    if request.method=="POST":
        form = CollegeForm(request.POST,request.FILES)
        if form.is_valid():
            College.objects.create(name=form.cleaned_data['name'],principal =form.cleaned_data['principal'],
                                   location= form.cleaned_data['location'],college_image=form.cleaned_data['college_image'])
        return redirect('college')
    return render(request,'college/addcollege.html',{'form':form})

def addstudent(request):
    form=StudentForm()
    if request.method == "POST":
        form= StudentForm(request.POST,request.FILES)
        if form.is_valid():
            Student.objects.create(name=form.cleaned_data['name'],college=form.cleaned_data['college'],
            branch=form.cleaned_data['branch'],semester=form.cleaned_data['semester'],
            student_image=form.cleaned_data['student_image'])
        return redirect('student')
    return render(request,'college/addstudent.html',{'form':form})
