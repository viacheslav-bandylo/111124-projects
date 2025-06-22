from django.http import HttpResponse

# Create your views here.
def hello_user(request):
    print(request.method)
    return HttpResponse("<h1>Hello, großpapa!</h1>")