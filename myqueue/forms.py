from django import forms

from .models import Lab, LabPart, Group


class LabForm(forms.ModelForm):

    class Meta:
        model = Lab
        fields = ('number', 'name')


class PartForm(forms.ModelForm):

    class Meta:
        model = LabPart
        fields = ('name',)


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('bench', 'names')
