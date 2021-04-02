from django import forms
from .models import Usuario, Segmento, Competencia


class ContactForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"
        # fields += Segmento.nome



class CompetenciaForm(forms.ModelForm):
    class Meta:
        mode = Competencia
        fields = "__all__"
