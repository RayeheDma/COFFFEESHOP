from django.shortcuts import render

def cafe(request):
    return render(request, 'index.html')