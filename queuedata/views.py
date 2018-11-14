from django.shortcuts import render
from .models import Lab

def lab_list(request):
    #labs = Lab.objects.all()
    return render(request, 'queuedata/lab_list.html', {})