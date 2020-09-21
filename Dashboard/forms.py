from django import forms
from StudentManager.models import Students

class staffForm(forms.Form):
    FirstName = forms.CharField(label='First Name', max_length=50, required=True)
    LastName = forms.CharField(label='Last Name', max_length=50, required=True)
    Email = forms.EmailField(label='Email', max_length=100, required=True)


class FilterStudentsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FilterStudentsForm, self).__init__(*args, **kwargs)
        self.fields['LastName'].required = False
        self.fields['FirstName'].required = False
        self.fields['ClassName'].required = False

    class Meta:
        model = Students
        fields = ('LastName', 'FirstName', 'ClassName')
        fields = ('LastName', 'FirstName', 'ClassName')