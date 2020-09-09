from django import forms
from StudentManager.models import CheckIn

class PassCodeForm(forms.Form):
    PassCode = forms.CharField(label='Pass Code', max_length=10, required=True)

class DenyEntryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DenyEntryForm, self).__init__(*args, **kwargs)
        self.fields['MetRequirements'].required = True
        self.fields['DenyEntryCheckIn'].required = True
        self.fields['ReasonCheckInPC'].required = True

    class Meta:

        model = CheckIn
        fields = ('MetRequirements', 'DenyEntryCheckIn', 'ReasonCheckInPC')

class admitForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(admitForm, self).__init__(*args, **kwargs)
        self.fields['MetRequirements'].required = True
        self.fields['PC'].required = True
        self.fields['Room'].required = True
        self.fields['AccompanyGuardian'].required = True
        self.fields['AccompanyGuardianPhone'].required = False
        self.fields['ReasonCheckInPC'].required = True

    class Meta:

        model = CheckIn
        fields = ('MetRequirements', 'PC', 'Room', 'AccompanyGuardian', 'AccompanyGuardianPhone', 'ReasonCheckInPC')