from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {'text':'template filter upper in use', 'number':100, 'text_2':'CUTcustom template filter in useCUT'}
    return render(request, 'app_templates/index.html', context_dict)

def other(request):
    return render(request, 'app_templates/other_page.html')

def url_templates_info(request):
    return render(request, 'app_templates/url_templates_info.html')
