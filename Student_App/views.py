from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from . import forms, models
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render,HttpResponse
from.models import *
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, "index.html")

def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect("/updateinput")
            else:
                return HttpResponse("You are not an admin.")
        else:
            alert = True
            return render(request, "admin_login.html", {'alert':alert})
    return render(request, "admin_login.html")

class InsertInput(View):
    def get(self,request):
        return render(request, 'Studentinput.html')
class InserView(View):
    def get(self,request):
        Student_Id = int(request.GET["t1"])
        Student_Name = request.GET["t2"]
        Student_Phone = request.GET["t3"]
        Student_Email = request.GET["t4"]
        DateOfBirth = request.GET["t5"]
        Graduation = request.GET["t6"]
        YearOfPass = request.GET["t7"]
        BatchName = request.GET["t8"]

        p1=Details(StudentId=Student_Id,StudentName=Student_Name,Phone=Student_Phone,Email=Student_Email,DateOfBirth=DateOfBirth,Graduation=Graduation,YearOfPass=YearOfPass,BatchName=BatchName)
        p1.save()
        resp=HttpResponse("Student inserted successfully")
        return resp
class DisplayView(View):
    def get(self,request):
        if 'q' in request.GET:
            q = request.GET['q']
            multiple_q = Q(Q(StudentId__icontains=q) | Q(StudentName__icontains=q))
            qs = Details.objects.filter(multiple_q)
        else:
            qs = Details.objects.all()

        con_dic={"records":qs}
        return render(request,"display.html",con_dic)

class DisplayresultView(View):
    def get(self,request):
        if 'r' in request.GET:
            r = request.GET['r']
            multiple_r = R(R(StudentId__icontains=r) | R(StudentName__icontains=r))
            rs = Results.objects.filter(multiple_r)
        else:
            rs = Results.objects.all()

        con_dic={"records":rs}
        return render(request,"Displayresult.html",con_dic)

class UpdateInputView(View):
    def get(self,request):
        return render(request,"updateinput.html")
class UpdateView(View):
    def post(self,request):
        Student_Id=int(request.POST["t1"])
        Student_Name = request.POST["t2"]
        Student_Phone = request.POST["t3"]
        Student_Email = request.POST["t4"]
        DateOfBirth=request.POST["t5"]
        Graduation = request.POST["t6"]
        YearOfPass = request.POST["t7"]
        BatchName = request.POST["t8"]
        Student =Details.objects.get(StudentId=Student_Id)
        Student.StudentName=Student_Name
        Student.StudentPhone = Student_Phone
        Student.StudentEmail = Student_Email
        Student.DateOfBirth = DateOfBirth
        Student.Graduation = Graduation
        Student.YearOfPass = YearOfPass
        Student.BatchName = BatchName


        Student.save()
        resp = HttpResponse("Student updated successfully")
        return resp

class DeleteInputView(View):
    def get(self,request):
        return render(request,"deleteinput.html")
class DeleteView(View):
    def get(self,request):
        Student_Id=int(request.GET["t1"])
        Student=Details.objects.filter(StudentId=Student_Id)
        Student.delete()
        resp = HttpResponse("Student deleted successfully")
        return resp

class ResultInput(View):
    def get(self,request):
        return render(request, 'resultinput.html')
class ResultView(View):
    def get(self,request):

        Student_Id = int(request.GET["t1"])
        Student_Name = request.GET["t2"]
        Id = Details.objects.get(StudentId=Student_Id)
        Name = Details.objects.get(StudentName=Student_Name)
        Subject1 = request.GET["t3"]
        Subject2 = request.GET["t4"]
        Subject3 = request.GET["t5"]
        Subject4 = request.GET["t6"]
        Subject5 = request.GET["t7"]
        Subject6 = request.GET["t8"]
        Total = request.GET["t9"]

        s = Results(StudentName=Student_Name,Subject1=Subject1,Subject2=Subject2,Subject3=Subject3,Subject4=Subject4,Subject5=Subject5,Subject6=Subject6,Total=Total)
        s.save()
        resp=HttpResponse("Student result inserted successfully")
        return resp







def Logout(request):
    logout(request)
    return redirect ("/")