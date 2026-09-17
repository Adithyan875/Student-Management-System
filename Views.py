from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def home(request):
    students = Student.objects.all()
    return render(request, "home.html", {"students": students})

def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST["name"],
            register_number=request.POST["register_number"],
            department=request.POST["department"],
            year=request.POST["year"],
            email=request.POST["email"],
            phone=request.POST["phone"],
            cgpa=request.POST["cgpa"]
        )
        return redirect("home")

    return render(request, "add_student.html")

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST["name"]
        student.register_number = request.POST["register_number"]
        student.department = request.POST["department"]
        student.year = request.POST["year"]
        student.email = request.POST["email"]
        student.phone = request.POST["phone"]
        student.cgpa = request.POST["cgpa"]
        student.save()

        return redirect("home")

    return render(request, "edit_student.html", {"student": student})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect("home")
