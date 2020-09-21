from django import forms
from StudentManager.models import Students

class ParentForm(forms.ModelForm):
    StudentName = forms.CharField(label='Student Name', max_length=100, disabled=True)

    def __init__(self, *args, **kwargs):
        super(ParentForm, self).__init__(*args, **kwargs)
        self.fields['Parent1'].required = True
        self.fields['Parent1Phone'].required = True
        self.fields['Parent1Address'].required = True
        self.fields['ParentPhoto'].required = True

    class Meta:
        model = Students
        fields = ('StudentName', 'Parent1', 'Parent1Phone', 'ParentEmail', 'Parent1Address',
                  'ParentPhoto', 'Alternative', 'Parent2', 'Parent2Phone', 'Parent2Address', 'OtherPhoto')