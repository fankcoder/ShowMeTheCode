from django.forms import ModelForm
from models import List

class CreateList(ModelForm):
    class Meta:
        model = List
        fields = ['title','content','level']
