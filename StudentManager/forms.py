from django import forms
from StudentManager.models import Students, Seasons, CurrentSeason

class FilterStudentsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FilterStudentsForm, self).__init__(*args, **kwargs)
        self.fields['LastName'].required = False
        self.fields['FirstName'].required = False
        self.fields['ClassName'].required = False

    class Meta:
        model = Students
        fields = ('LastName', 'FirstName', 'ClassName')

class StudentsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentsForm, self).__init__(*args, **kwargs)
        self.fields['SID'].required = False
        self.fields['DateOfBirth'].required = False
        self.fields['YearGroup'].required = False
        self.fields['photo'].required = False
        self.fields['Term'].required = False
        self.fields['ClassName'].required = False
        self.fields['DateOfAdmission'].required = False
        self.fields['AcademicSession'].required = False
        self.fields['Parent1'].required = False
        self.fields['Parent2'].required = False
        self.fields['Parent1Phone'].required = False
        self.fields['Parent2Phone'].required = False
        self.fields['Parent1Address'].required = False
        self.fields['Parent2Address'].required = False

    class Meta:

        model = Students
        fields = ('SID', 'FirstName', 'MiddleName', 'LastName', 'Gender', 'DateOfBirth', 'YearGroup', 'photo', 'Term', 'ClassName',
                  'DateOfAdmission', 'AcademicSession', 'Parent1', 'Parent1Phone', 'ParentEmail', 'Parent1Address',
                  'Parent2',  'Parent2Phone', 'Parent2Address')

        widgets = {
            'DateOfBirth': forms.DateInput(format=('%m/%d/%Y'),
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
            'DateOfAdmission': forms.DateInput(format=('%m/%d/%Y'),
                                           attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                  'type': 'date'}),
        }
