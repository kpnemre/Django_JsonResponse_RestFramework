from django import forms
from django.forms import fields
from .models import Student

# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)
#     number = forms.IntegerField() 

class StudentForm(forms.ModelForm):
    first_name=forms.CharField(label='Your Name')
    # override ediyor
    class Meta:
        model= Student
        # Tupple içinde yazıyoruz
        # fields= ("first_name", "last_name", "number")
        fields= '__all__'
        #2. yöntem
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['last_name'].label= "Sir Name"