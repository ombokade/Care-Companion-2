from django import forms

class PatientForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()

    gender = forms.ChoiceField(
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other')
        ]
    )