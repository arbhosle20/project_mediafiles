from django import forms
from .models import Laptop
from django.core import validators

class LaptopModelForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'

        #labels
        labels = {
            'ram' : 'RAM in GB ',
            'rom': 'ROM',
            'model_name':'Model Name'
        }

        # placeholder
        widgets = {'company':forms.TextInput(attrs={'placeholder':'e.g : dell,lenovo'}),
                   'model_name': forms.TextInput(attrs={'placeholder': 'eg : thinkPad,lattitude'}),
                   'ram': forms.NumberInput(attrs={'placeholder': 'eg : 2GB,4GB,8GB'}),
                   'rom':forms.NumberInput(attrs={'placeholder':'eg : 1SSD'}),
                   'processor':forms.TextInput(attrs={'placeholder':'eg : core i3,Xeon'}),
                   'price':forms.NumberInput(attrs={'placeholder':'Enter the price'}),
                   'weigth':forms.NumberInput(attrs={'placeholder':'eg : 2kg'})
                   }



    def clean(self):
        all_cleaned_data = super().clean()

        # for rom

        r = all_cleaned_data['rom']
        if r<1:
            raise forms.ValidationError("ROM can not be less than 1!")
        elif r%2==0:
            raise forms.ValidationError("ROM always available in Odd number")

        # for ram

        p =all_cleaned_data['ram']
        if p  not in  [2,4,6,8,16,24,64,256]:
            raise forms.ValidationError("please enter valid RAM")

        #for weigth

        w = all_cleaned_data['weigth']
        if w<0:
            raise forms.ValidationError("weight can not be negative")

