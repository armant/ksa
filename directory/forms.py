from django import forms
from models import KSA

class KSAForm(forms.ModelForm):
    class Meta:
        model = KSA
        fields = ('ksa_name', 'president_name', 'president_contact', 'president_photo', 'key_people', 'housing_info', 'facebook_group', 'note', )