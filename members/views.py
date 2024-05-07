from django.shortcuts import render, redirect,HttpResponse
from .models import Member 
from .forms import ProjectForm
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate , login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# @login_required(login_url='login')
def home(request):
    form = ProjectForm()
    context={
        'form':form,
    }
    return render(request, "home.html",context)



def test(request):  
    return render(request,'test.html')




def signup(request):
    if request.method =="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Sizning tergan parolingiz  parolingizga bilan bir-xil emas!!")
        else:
            user = User.objects.create_user(username, email, pass1)
            user.save()
            return redirect("login")

    return render(request, 'signup.html')


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, 'Foydalanuvchi nomi yoki parol noto`g`ri.')
            return render(request, 'login.html')  # Render login page with error message
    else:
        return render(request, 'login.html')  # Render login page for GET requests


def LogoutPage(request):
    logout(request)
    return redirect('login')

def project_add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm()

    data = Member.objects.all()
    context = {
        'form': form,
        'data': data,
    }
    return render(request, "project_add.html", context)
    

def project_show(request):
    data=Member.objects.all()
    context = {
        'data':data,
    }
    return render(request, "projects.html", context)     



