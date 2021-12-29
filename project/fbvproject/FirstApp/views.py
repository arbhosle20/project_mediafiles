from django.shortcuts import render,redirect
from .models import Laptop
from .forms import LaptopModelForm
from django.contrib.auth.decorators import login_required
from django.views import View

# Create your views here.
class addLaptopView(View):
    def get(self,request):
        form = LaptopModelForm()
        template_name = 'FirstApp/addlaptop.html'
        context = {'form': form}
        return render(request, template_name, context)

    def post(self,request):
        form = LaptopModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show')
        template_name = 'FirstApp/addlaptop.html'
        context = {'form': form}
        return render(request, template_name, context)

def showLaptopView(request):
    lap_object = Laptop.objects.all()
    template_name = 'FirstApp/showlaptop.html'
    context = {'lap_object':lap_object}
    return render(request, template_name, context)

@login_required(login_url='login')
def updateView(request,id):
    lap_object = Laptop.objects.get(id=id)
    form = LaptopModelForm(instance=lap_object)
    if request.method == 'POST':
        form = LaptopModelForm(request.POST,form)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = 'FirstApp/addlaptop.html'
    context = {'form':form}
    return render(request, template_name, context)

@login_required(login_url='login')
def deleteView(request,id):
    lap_object = Laptop.objects.get(id=id)
    if request.method == 'POST':
        lap_object.delete()
        return redirect('show')
    template_name = 'FirstApp/deletelaptop.html'
    context = {'lap_object':lap_object}
    return render(request, template_name, context)

def details(request,id):
    lap_object = Laptop.objects.get(id=id)
    template_name = 'FirstApp/detailslaptop.html'
    context = {'lap_object': lap_object}
    return render(request, template_name, context)
