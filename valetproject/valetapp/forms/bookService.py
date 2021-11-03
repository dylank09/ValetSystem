from django import forms

class AvailabilityForm(forms.Form):
    VALET_CATERGORIES=(
        ('WXW', 'Wax&Wash'),
        ('INW', 'Interior&Wash'),
        ('PWH', 'Polish&Wash'),
        ('ALL', 'All'),
        ('WAS', 'Wash')
    )
    valet_services = forms.ChoiceField(choices=VALET_CATERGORIES, required=True)
    start_time = forms.DateTimeField(required=True, input_formats=['%H:M'])
    end_time = forms.DateTimeField(required=True, input_formats=['%H:M'])