from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Details(models.Model):
    StudentId = models.IntegerField(primary_key=True)
    StudentName = models.CharField(max_length=50, null=True)
    Phone = models.IntegerField(null=True)
    Email = models.CharField(max_length=50,null=True)
    DateOfBirth = models.DateField()
    Graduation = models.CharField(max_length=100,null=True)
    YearOfPass = models.IntegerField( null=True)
    BatchName = models.CharField(max_length=100)


    def __str__(self):
        return self.StudentName
class Results(models.Model):
    Details = models.ForeignKey(Details,on_delete=models.CASCADE)
    StudentName= models.CharField(max_length=100,null=True)
    Subject1= models.CharField(max_length=100,null=True)
    Subject2 = models.CharField(max_length=100, null=True)
    Subject3 = models.CharField(max_length=100, null=True)
    Subject4 = models.CharField(max_length=100, null=True)
    Subject5 = models.CharField(max_length=100, null=True)
    Subject6 = models.CharField(max_length=100, null=True)
    Total = models.CharField(max_length=100,null=True)


    def __str__(self):
        return self.Subject1