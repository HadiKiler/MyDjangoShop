from django import forms
from .models import item

class newItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = (['type','name','dis','price','img1','img2','off'])
        widgets = {
            'type':forms.Select(attrs={'class':'rounded'}),
            'name':forms.TextInput(attrs={'class':'rounded'}),
            'dis':forms.Textarea(attrs={'class':'rounded'}),
            'price':forms.TextInput(attrs={'class':'rounded'}),
            'img1':forms.FileInput(attrs={'class':'rounded'}),
            'img2':forms.FileInput(attrs={'class':'rounded'}),
            'off':forms.TextInput(attrs={'class':'rounded'}),
        }

class editItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = (['type','name','dis','price','img1','img2','off'])
        widgets = {
            'type':forms.Select(attrs={'class':'rounded'}),
            'name':forms.TextInput(attrs={'class':'rounded'}),
            'dis':forms.Textarea(attrs={'class':'rounded'}),
            'price':forms.TextInput(attrs={'class':'rounded'}),
            'img1':forms.FileInput(attrs={'class':'rounded'}),
            'img2':forms.FileInput(attrs={'class':'rounded'}),
            'off':forms.TextInput(attrs={'class':'rounded'}),
        }