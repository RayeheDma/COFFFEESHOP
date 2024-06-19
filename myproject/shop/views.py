from django.shortcuts import render



def welcome_to_cafe(request):
    return render(request, 'index.html')
