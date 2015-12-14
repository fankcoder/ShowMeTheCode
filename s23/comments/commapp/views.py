from django.shortcuts import render
from commapp.models import comdata

from forms import CommentForm

def index(request):
    if request.method=='request.POST':
        form = CommentFrom(request.POST)
        if form.is_vaild():
            print 'get data'
    else:
        form = CommentForm()

    #print form.username
    #print type(data)
    #print data['user']
    #username = CommentFrom.username(data['username'])
    #usercomment = CommentFrom.usercomment(data['usercomment'])
    
    #if form.is_valid():
    #    return 
    return render(request,'index.html',{'form':form})
