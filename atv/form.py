from dataclasses import field, fields
from django.forms import ModelForm
from .models import Compra, Compra1, Compra2, Compra3

class Compraform(ModelForm):
    class Meta:
        model = Compra
        fields = ['peca', 'cor']

class Compraform1(ModelForm):
    class Meta:
        model = Compra1
        fields = ['peca', 'cor']

class Compraform2(ModelForm):
    class Meta:
        model = Compra2
        fields = ['peca', 'cor']

class Compraform3(ModelForm):
    class Meta:
        model = Compra3
        fields = ['peca', 'cor']