from django import forms
from .models import Insured, Insurance, InsuranceEvent

class InsuredForm(forms.ModelForm):

    class Meta:
        model = Insured
        fields = ["name", "address", "email", "phone"]
class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = ["insured_person", "policy_type", "start_date", "end_date"]

class InsuranceEventForm(forms.ModelForm):
    class Meta:
        model = InsuranceEvent
        fields = ["insurance", "event_date", "description"]
