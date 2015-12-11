from django import forms

class CommentFrom(forms.Form):
    username = forms.CharField(max_length=20)
    usercomment = forms.CharField(max_length=1200)
    
