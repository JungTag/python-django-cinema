from django.shortcuts import render, redirect

# Create your views here.
def initialize_DB(request):
    return redirect('index')

def index(request):
    return render(request, 'index.html')