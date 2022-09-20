from dataclasses import fields
from django import forms
from test_app.models import User

class NewUserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = '__all__'