# forms.py
from django import forms
from .models import User
# from django.db.models import Q


class ShareThoughtForm(forms.Form):
    shared_with = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,  # Users are not required to select anyone
    )

    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user', None)
    #     super(ShareThoughtForm, self).__init__(*args, **kwargs)
        
    #     if user:
    #         self.fields['shared_with'].queryset = User.objects.exclude( Q(id=user.id) | Q(is_superuser=True))
