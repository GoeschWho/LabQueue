from .models import Lab, Group
from django.shortcuts import render, get_object_or_404, redirect
from .forms import LabForm, PartForm, GroupForm, HelpForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import JsonResponse


def home(request):
    return render(request, 'myqueue/home.html')


def lab_list(request):
    labs = Lab.objects.all()
    return render(request, 'myqueue/lab_list.html', {'labs': labs})


def lab_detail(request, pk):
    lab = get_object_or_404(Lab, pk=pk)
    return render(request, 'myqueue/lab_detail.html', {'lab': lab})


@login_required
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


@login_required
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


@login_required
def lab_remove(request, pk):
    lab = get_object_or_404(Lab, pk=pk)
    lab.delete()
    return redirect('lab_list')


@login_required
def add_part_to_lab(request, pk):
    lab = get_object_or_404(Lab, pk=pk)
    if request.method == "POST":
        form = PartForm(request.POST)
        if form.is_valid():
            part = form.save(commit=False)
            part.lab = lab
            part.save()
            return redirect('lab_detail', pk=lab.pk)
    else:
        form = PartForm()
    return render(request, 'myqueue/add_part_to_lab.html', {'form': form})


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'myqueue/group_list.html', {'groups': groups})


def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(request, 'myqueue/group_detail.html', {'group': group})


@login_required
def group_new(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            #code generated fields
            group.save()
            return redirect('group_detail', pk=group.pk)
    else:
        form = GroupForm()
    return render(request, 'myqueue/group_edit.html', {'form': form})


def group_edit(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == "POST":
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save(commit=False)
            #code generated fields
            group.save()
            return redirect('group_detail', pk=group.pk)
    else:
        form = GroupForm(instance=group)
    return render(request, 'myqueue/group_edit.html', {'form': form})


@login_required
def group_remove(request, pk):
    group = get_object_or_404(Group, pk=pk)
    group.delete()
    return redirect('group_list')


def help_queue(request):
    groups = Group.objects.filter(help=True).order_by('position')
    return render(request, 'myqueue/help_queue.html', {'groups': groups})


def help_list(request):
    groups = Group.objects.all()
    return render(request, 'myqueue/help_list.html', {'groups': groups})


def help_edit(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == "POST":
        form = HelpForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save(commit=False)
            # code generated fields
            group.time = timezone.now()
            group.save()
            if group.help:
                if group.position == 0: # not already in queue (re-saved)
                    group.list_add()
                return redirect('help_queue')
            else:
                group.list_remove()
                return redirect('help_edit', pk=group.pk)
    else:
        form = HelpForm(instance=group)
    return render(request, 'myqueue/help_edit.html', {'form': form})


def status_list(request):
    groups = Group.objects.all()
    return render(request, 'myqueue/status_list.html', {'groups': groups})
