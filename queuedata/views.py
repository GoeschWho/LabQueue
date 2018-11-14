from django.shortcuts import render

def lab_list(request):
    return render(request, 'queuedata/lab_list.html', {})