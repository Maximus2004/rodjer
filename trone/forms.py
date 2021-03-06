from django import forms
from .models import DuoReg, PraksReg, Pay, SquadsReg


class DuoForm(forms.ModelForm):
    class Meta:
        model = DuoReg
        fields = ('username1', 'username2',)


class PraksForm(forms.ModelForm):
    class Meta:
        model = PraksReg
        fields = ('name', 'username1', 'vk1', 'username2', 'username3', 'username4', 'reserv1', 'reserv2',)


class SquadsForm(forms.ModelForm):
    class Meta:
        model = SquadsReg
        fields = ('username1', 'username2', 'username3', 'username4',)


class PayForm(forms.ModelForm):
    class Meta:
        model = Pay
        fields = ('username', 'vk',)
