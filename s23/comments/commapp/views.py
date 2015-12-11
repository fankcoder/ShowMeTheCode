from django.shortcuts import render
from commapp.models import comdata
from forms import CommentFrom

def index(request):
    data = request.GET
    if request.is_valid():
        print data['username']
        print data['usercomment']
        #username = CommentFrom.username(data['username'])
        #usercomment = CommentFrom.usercomment(data['usercomment'])
        
        #if form.is_valid():
        #    return 
    return render(request,'index.html')
