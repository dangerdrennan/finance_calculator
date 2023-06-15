from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['current_age', 'retirement_age', 'current_salary', 'current_savings', 'rate_of_return']
