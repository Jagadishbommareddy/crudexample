from django import forms
from empolyee.models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"