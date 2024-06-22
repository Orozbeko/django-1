from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(required=True)
    address = forms.CharField(required=True)
    date_of_birth = forms.DateField(required=True)
    gender = forms.CharField(required=True)
    occupation = forms.CharField(required=True)
    company = forms.CharField(required=True)
    biography = forms.CharField(required=True)
    website = forms.URLField(required=True)
    twitter_handle = forms.CharField(required=True)
    linkedin_profile = forms.URLField(required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            'phone_number'
            'address'
            'date_of_birth'
            'gender'
            'occupation'
            'company'
            'biography'
            'website'
            'twitter_handle'
            'linkedin_profile'
        )
    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=True)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

@receiver(post_save, sender=models.CustomUser)
def set_experience(sender, instance, created, **kwargs):
    if created:
        print("Сигнал обработан успешно пользователь зарегистрировался")
        age = instance.age
        if age < 1:
            instance.experience = 'Junior'
        elif age >= 2 and age <= 3:
            instance.experience = 'Junior'
        elif age >= 3 and age <= 5:
            instance.experience = 'Middle'
        else:
            instance.experience = 'Senior'
        instance.save()

