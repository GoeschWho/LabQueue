from .models import Lab
from django.shortcuts import render, get_object_or_404


def lab_list(request):
    labs = Lab.objects.all()
    return render(request, 'queue/lab_list.html', {'labs': labs})


def lab_detail(request, pk):
    lab = get_object_or_404(Lab, pk=pk)
    return render(request, 'queue/lab_detail.html', {'lab': lab})
