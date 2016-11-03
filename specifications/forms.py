from django import forms

from .models import Setup, Specification


class SetupForm(forms.ModelForm):

    def clean(self):
         cleaned_data = super(SetupForm, self).clean()
         description = cleaned_data.get('description', None)
         if description is None or len(description)> 100:
             raise forms.ValidationError('Description should be less than 100 characters')


    class Meta:
        model = Setup
        fields = '__all__'


class SpecificationForm(forms.ModelForm):
    class Meta:
        model = Specification
        fields = '__all__'
