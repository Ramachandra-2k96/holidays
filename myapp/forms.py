from django import forms
class inputform(forms.Form):
    choice=(("KA","Karnataka"), ("MH", "Maharashtra"))
    stateinput=forms.ChoiceField(choices=choice, label="Select State")
