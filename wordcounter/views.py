from django.shortcuts import render
from django .http import HttpResponse

# Create your views here.
def home(request):
    result=0
    if request.method=='POST':
        text=request.POST.get('text' , '')
        result=len(text.split())
    return render(request, 'home.html' , {'result': result})
