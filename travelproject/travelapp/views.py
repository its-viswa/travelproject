from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Guides


# Create your views here.
def demo(request):
  obj=Place.objects.all()
  obj1=Guides.objects.all()
  return  render(request,"index.html",{'result':obj,'test':obj1})

