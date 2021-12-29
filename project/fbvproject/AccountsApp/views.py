from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def loginView(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        print(un)
        print(pw)
        user = authenticate(username=un,password=pw)
        if user is not None:
            login(request,user)
            return redirect('show')
        else:
            messages.error(request,'Invalid Credentials !')
    context = {}
    template_name = 'AccountsApp/login.html'
    return render(request, template_name, context)

def registrationView(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form':form}
    template_name = 'AccountsApp/register.html'
    return render(request, template_name, context)



def logoutView(request):
    logout(request)
    return redirect('login')