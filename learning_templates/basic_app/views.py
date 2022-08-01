from django.shortcuts import render

# Create your views here.

def index(request):
    contex = {'greet': 'hello world again!'}
    return render(request,'basic_app/index.html', contex)

def other_1(request):
    return render(request,'basic_app/other1.html')

def other_2(request):
    return render(request,'basic_app/other2.html')

def other_3(request):
    return render(request,'basic_app/other3.html')

def relative(request):
    return render(request,'basic_app/relative_url_template.html')