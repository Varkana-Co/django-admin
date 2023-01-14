from django.http import HttpResponse

def index(request):
    #bodey
    return HttpResponse('<h1>Hello dear samira</h1>')


def home(request):
    return HttpResponse('<h3>Wellcom to my Website.....')
