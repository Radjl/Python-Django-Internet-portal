from django import forms
from django.forms import ModelForm, Textarea, CharField, TextInput

from .models import Ship, Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from tinymce.widgets import TinyMCE

class ShipAdd(forms.Form):
    Id = forms.IntegerField(required=False)
    Name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    Photo = forms.ImageField(required=False)
    Info = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    Content = forms.CharField(widget=SummernoteWidget(attrs={'width': '100%', 'height': '250px'}),required=False)
    ContentEng = forms.CharField(widget=SummernoteWidget(attrs={'width': '100%', 'height': '250px'}),required=False)
    Pubdate = forms.DateTimeField(required=False)



class shipadd2(ModelForm):
    class Meta:
        model = Ship
        fields = {'Name','Info','Content','ContentEng'}
        widgets = {
            'Name': TextInput(attrs={"class":"form-control"}),
            'Info': TextInput(attrs={"class": "form-control"}),
            'Content': SummernoteWidget(attrs={'width': '100%', 'height': '250px'}),
            'ContentEng': SummernoteWidget(attrs={'width': '100%', 'height': '250px'}),





        }


class CommentForm(forms.Form):
    Content = forms.CharField(
        label="1",
        widget=forms.Textarea
    )

    ContentExtended = forms.CharField(
        label="2",
        widget=forms.Textarea,
        required=False
    )



