from django.shortcuts import render
from .forms import CreateList
from .models import List


# Create your views here.
def index(request):
    form = CreateList()
    
    if request.method=='POST':
        form = CreateList(request.POST)
        if form.is_valid():
            form.save()
            data = List.objects.all()[::-1]
            context = {'data':data}
            for each in  data:
                print each.levelist[0]
            return render(request,'index.html',context)

    elif 'del' in request.GET:
        print request.GET['del']
        id_num = request.GET['del']
        List.objects.filter(id=id_num).delete()
        data = List.objects.all()[::-1]
        context = {'data':data}
        return render(request,"index.html",context)

    return render(request,'index.html')
