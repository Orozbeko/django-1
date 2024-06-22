from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(User):
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=255)
    date_of_birth = models.DateField('Укажите дату рождение')
    gender = models.CharField(max_length=10)
    occupation = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    biography = models.TextField(verbose_name='Опишите себя')
    website = models.URLField('Укажите ссылку на вебсайт')
    twitter_handle = models.CharField(max_length=15)
    linkedin_profile = models.URLField()

@receiver(post_save, sender=CustomUser)
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


