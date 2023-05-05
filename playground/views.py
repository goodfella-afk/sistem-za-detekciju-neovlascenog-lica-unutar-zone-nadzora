from django.shortcuts import render
from django.http import HttpResponse
from .models import Sistem
from django.shortcuts import redirect

# Create your views here.

#sistemDBmysql
def say_hello(request):
    sistems = Sistem.objects.all()

    context = {
        'sistems':sistems
    }
    return render(request, 'hello.html', context)


def reqReboot(request):
    newValue=3
    Sistem.objects.filter(aktivnost="kameramon").update(status=newValue)
    response = redirect('/')
    return response






#datetimehour

# def home(request):
#     date = datetime.now()

#     context = {
#         'date':date
#     }
#     return render(request, 'hello.htm',context)