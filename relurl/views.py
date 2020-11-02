from django.shortcuts import render

def index(request):
    return render(request,'relurl/index.html')
def other(request):
    return render(request,'relurl/other.html')
def rel_url(request):
    return render(request,'relurl/relurl.html')
