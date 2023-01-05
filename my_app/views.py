from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): 
     return HttpResponse('Hi how is it going?')

def showProduct(request): 
     return HttpResponse('Product for page 2')