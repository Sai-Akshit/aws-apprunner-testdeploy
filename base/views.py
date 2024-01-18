from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello from Akshith &#128520;</h1>")
