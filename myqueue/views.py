from .models import Lab
from django.shortcuts import render, get_object_or_404, redirect
from .forms import LabForm


def lab_list(request):
    labs = Lab.objects.all()
    return render(request, 'myqueue/lab_list.html', {'labs': labs})


def lab_detail(request, pk):
    lab = get_object_or_404(Lab, pk=pk)
    return render(request, 'myqueue/lab_detail.html', {'lab': lab})


def lab_new(request):
    if request.method == "POST":
        form = LabForm(request.POST)
        if form.is_valid():
            lab = form.save(commit=False)
            #code generated fields
            lab.save()
            return redirect('lab_detail', pk=lab.pk)
    else:
        form = LabForm()
    return render(request, 'myqueue/lab_edit.html', {'form': form})


def lab_edit(request, pk):
    lab = get_object_or_404(Lab, pk=pk)
    if request.method == "POST":
        form = LabForm(request.POST, instance=lab)
        if form.is_valid():
            lab = form.save(commit=False)
            #code generated fields
            lab.save()
            return redirect('lab_detail', pk=lab.pk)
    else:
        form = LabForm(instance=lab)
    return render(request, 'myqueue/lab_edit.html', {'form': form})
