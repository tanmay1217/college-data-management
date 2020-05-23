from django.db import models

# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=100)
    location = models.CharField(max_length=256)
    college_image = models.ImageField(upload_to = 'college/')
    def __str__(self):
        return '{}'.format(self.name)
class Student(models.Model):
    name= models.CharField(max_length=256)
    college= models.ForeignKey(College,on_delete=models.CASCADE)
    branch= models.CharField(max_length=25)
    semester= models.IntegerField()
    student_image = models.ImageField(upload_to= 'student/')
    def __str__(self):
        return '{}'.format(self.name)
