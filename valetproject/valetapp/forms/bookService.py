from django import forms
from ..models.valet import Valet


class AvailabilityForm(forms.Form):
    valetObjects = Valet.objects.all()
    VALET_CATERGORIES = []
    for valet in valetObjects:
        VALET_CATERGORIES.append((valet, valet.getName()))
    VALET_CATERGORIES = tuple(VALET_CATERGORIES)
    valet_services = forms.MultipleChoiceField(
        choices=VALET_CATERGORIES, required=True)
    start_time = forms.DateTimeField(required=True, input_formats=['%H:%M'])
