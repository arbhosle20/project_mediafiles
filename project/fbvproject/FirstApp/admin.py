from django.contrib import admin
from .models import Laptop

# Register your models here.

class LaptopAdmin(admin.ModelAdmin):
    list_display = ['id','company','model_name','ram','rom','processor','price','weigth']
admin.site.register(Laptop,LaptopAdmin)