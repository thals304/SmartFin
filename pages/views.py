from django.shortcuts import render

def mainpage(request):
    return render(request, 'pages/index.html')

def company(request):
    return render(request, 'pages/company_info.html')
