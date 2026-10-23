from django import forms
from .models import Material

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['id_material', 'name', 'description', 'unit', 'material_type', 'status']