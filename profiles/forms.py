from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'location', 'image']

    def clean(self):
        cleaned_data = super().clean()
        image = cleaned_data.get('image')
        if not image:
            raise forms.ValidationError("Profile image is required.")
        return cleaned_data

    def signup(self, request, user):
        user.save()
        profile = Profile()
        profile.user = user
        profile.name = self.cleaned_data['name']
        profile.location = self.cleaned_data['location']
        profile.image = self.cleaned_data['image']
        profile.save()
