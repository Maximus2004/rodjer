from django import forms
from .models import EasyReg, EasyReg2, Pay


class EasyForm(forms.ModelForm):
    class Meta:
        model = EasyReg
        fields = ('username1', 'username2',)


class EasyForm2(forms.ModelForm):
    class Meta:
        model = EasyReg2
        fields = ('username1', 'username2', 'username3', 'username4',)


class PayForm(forms.ModelForm):
    class Meta:
        model = Pay
        fields = ('username', 'vk',)
