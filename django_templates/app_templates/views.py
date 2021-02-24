from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app_templates/index.html')

def other(request):
    return render(request, 'app_templates/other_page.html')

def url_templates_info(request):
    return render(request, 'app_templates/url_templates_info.html')
