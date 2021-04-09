from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['polyclinic', 'doctor', 'visit_time', 'full_name', 'policy_number']