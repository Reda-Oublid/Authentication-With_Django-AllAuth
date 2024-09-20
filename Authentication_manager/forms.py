from django import forms

from Authentication_manager.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'bio', 'birthdate', 'phone_number', 'country', 'preferences',)
        widgets = {
            'preferences': forms.Select(attrs={
                'class': 'form-element'
            }),
            'bio': forms.Textarea(attrs={
                'rows': 3,
                'cols': 50,
                'class': 'form-element'
            }),

            'birthdate': forms.DateInput(format='%Y-%m-%d', attrs={
                'class': 'form-element'
            }),

            'phone_number': forms.NumberInput(attrs={
                'class': 'form-element'
            }),

            'country': forms.TextInput(attrs={
                'class': 'form-element'
            })
        }
