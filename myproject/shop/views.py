from django.shortcuts import HttpResponse


# Display "welcome" to the web page
def welcome_to_cafe(request):
    return HttpResponse("<h1>welcome</h1>")
