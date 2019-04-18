from django.shortcuts import render

def intro_index(request):
    template_name = 'intro/index.html'

    return render(request, 'intro/index.html')