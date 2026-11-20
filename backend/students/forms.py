from django import forms
from .models import Students

class StudentsForm(forms.ModelForm):

    class Meta:
        model = Students
        fields = [
            'name',
            'email',
            'age',
            'department'
        ]
        from django import forms
from .models import Students

