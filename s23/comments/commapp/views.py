from django.shortcuts import render,render_to_response
from .forms import Comment
from .models import CommentData

def index(request):
    form = Comment()
    if request.method=='POST':
        form = Comment(request.POST)
        if form.is_valid():
            form.save()
            comment = CommentData.objects.all()[::-1]
            for each in comment:
                pass#print each.name,each.create_time
            connect = {'form':form,'comment':comment}
            return render(request,"index.html", connect)
    else:
        form = Comment()

    #print form.username
    #print type(data)
    #print data['user']
    #username = CommentFrom.username(data['username'])
    #usercomment = CommentFrom.usercomment(data['usercomment'])
    
    #if form.is_valid():
    #    return 
    return render(request,'index.html',{'form':form})
