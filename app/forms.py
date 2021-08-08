from django import forms
from app.models import ProductModel
class Productform(forms.ModelForm):
    #pname = forms.CharField(widget=forms.TextInput(attrs={"style":'font-size:20px;'}))
    #price = forms.IntegerField(widget=forms.NumberInput(attrs={"style": 'font-size:20px;'}))
    #quantity = forms.IntegerField(widget=forms.NumberInput(attrs={"style": 'font-size:20px;'}))

    class Meta:
      model = ProductModel
      fields = '__all__'