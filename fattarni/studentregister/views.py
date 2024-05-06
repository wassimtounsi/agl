from django.shortcuts import render, redirect
from .forms import StudentForm, SignInForm
from .models import students
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import FormSubmissionForm
from .models import menu


from django.contrib.auth import authenticate, login

def student_list(request):
    context = {'student_list': students.objects.all()}
    return render(request, "studentregister/student_list.html", context)

def student_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = StudentForm()
        else:
            student_obj = students.objects.get(pk=id)
            form = StudentForm(instance=student_obj)
        
        return render(request, "studentregister/student_form.html", {'form': form})
    else:
        if id == 0:
            form = StudentForm(request.POST)
        else:
            student_obj = students.objects.get(pk=id)
            form = StudentForm(request.POST, instance=student_obj)
        
        if form.is_valid():
            form.save()
            return redirect("home")

def student_delete(request,id):
    student_obj = students.objects.get(pk=id)
    student_obj.delete()
    return redirect("/student/list")

def student_sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['fullname']
            password = form.cleaned_data['password']
            try:
                if username == "sudo" and password == "sudo":
                    return redirect("admin_choose")

                student_obj = students.objects.get(fullname=username)

                if(student_obj.password == password):
                    # Passwords match, redirect to home page
                    return redirect("home")
                else:
                    # Passwords don't match, stay on sign-in page and refresh
                    return render(request, 'studentregister/signIn.html', {'form': form})
            except students.DoesNotExist:
                # Student does not exist, redirect to sign-up page
                return redirect("student_insert")
    else:
        form = SignInForm()
    return render(request, 'studentregister/signIn.html', {'form': form})



def home_view(request):
    return render(request, 'studentregister/resto1-main/user/home.html')

def student_signup(request):
    return redirect("student_insert")
def student_login(request):
    return redirect("student_sign_in")
def options_view(request):
    return render(request, 'studentregister/options.html')
def menu_view(request):
        print ('Adding')
        if request.method == 'POST':
            form = FormSubmissionForm(request.POST)
            if form.is_valid():
                form.save()
                print("Form saved successfully!")  # Add debug output
                return redirect("home")
            else:
                print(form.errors)  # Print form errors for debugging
        else:
            form = FormSubmissionForm()

        return render(request,'studentregister/resto1-main/admin/add-menu.html')
def about_view(request):
    return render(request,'studentregister/resto1-main/user/about.html')

def add_menu(request):
    print ('Adding')
    if request.method == 'POST':
        form = FormSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form saved successfully!")  # Add debug output
            return redirect("home")
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = FormSubmissionForm()

    print(request.POST)  # Print POST data for debugging
    return render(request, 'studentregister/resto1-main/user/menu.html', {'form': form})

def menu_list_view(request):
    context = {'menu_items': menu.objects.all()} 
    return render(request, "studentregister/resto1-main/user/menu.html", context)