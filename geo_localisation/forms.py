from django import forms


class SelectionBatimentForm(forms.Form):
    batiment = forms.CharField(label='batiment', widget=forms.CheckboxInput)
