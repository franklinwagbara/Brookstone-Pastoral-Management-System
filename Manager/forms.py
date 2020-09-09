from django import forms
from StudentManager.models import Students, Seasons, CurrentSeason

class CurrentSeasonForm(forms.ModelForm):
    class Meta:
        model = CurrentSeason
        fields = ['Season',]

    def __init__(self, *args, **kwargs):
        super(CurrentSeasonForm, self).__init__(*args, **kwargs)
        self.fields['Season'] = forms.ModelChoiceField(queryset=Seasons.objects.all())

class SeasonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SeasonForm, self).__init__(*args, **kwargs)
        self.fields['SeasonName'].required = False
        self.fields['Date'].required = False

    class Meta:

        model = Seasons
        fields = ('SeasonName', 'Date')

        widgets = {
            'Date': forms.DateInput(format=('%m/%d/%Y'),
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'})
        }

