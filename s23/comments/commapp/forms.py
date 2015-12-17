'''
from django import forms

class CommentForm(forms.Form):
    username = forms.CharField(label='Your name',max_length=20)
    usercomment = forms.CharField(label='Your comment',max_length=1200)
'''

from django.forms import ModelForm
from models import CommentData

class Comment(ModelForm):
    class Meta:
        model = CommentData
        fields = ['name','comments']
