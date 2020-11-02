from django.shortcuts import render
from Users.forms import Userprofile
def index(request):
    return render(request,'index.html')

def form_view(request):
    form=Userprofile()

    if request.method =="POST":
        form = Userprofile(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR')
        
    return render(request,'form.html',{'form':form})
