from django.shortcuts import render



def main_page(request):
    ctx = {}
    return render(request, 'main_page/index.html', ctx)
