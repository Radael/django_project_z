from crispy_forms.helper import FormHelper
from django import forms
from django.forms import DateInput
from django_countries.widgets import CountrySelectWidget
from django.core.validators import RegexValidator
from .models import *
from django_countries.widgets import CountrySelectWidget


class DotaTournamentTierSearch(forms.Form):
    TIER_CHOICES = [
        (0, 'All'),
        (1, 'International'),
        (2, 'Major'),
        (3, 'DPC'),
        (4, 'Other'),
    ]

    dotatournament_tier = forms.ChoiceField(
        label='Поиск по тиру турнира',
        required=False,
        choices=TIER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select', 'placeholder': 'Поиск'})
    )
    # dotatournament_tier.widget.attrs.update({'placeholder': 'Поиск'})


class AddTeamForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        model = DotaTeam
        fields = '__all__'


class AddPlayerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['born'].widget.input_type = 'date'

    class Meta:
        model = DotaPlayer
        fields = '__all__'


class AddTournamentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['event_date'].widget.input_type = 'date'
        self.fields['end_event_date'].widget.input_type = 'date'

    class Meta:
        model = DotaTournament
        fields = '__all__'

