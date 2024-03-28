from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User



class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Category name')
    def __str__(self):
        return self.title


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='choices')
    question = models.CharField(verbose_name="question", max_length=250)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.question
 

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(verbose_name="choice", max_length=100)
    is_correct = models.BooleanField(default=False, verbose_name="Right answer")
    position = models.IntegerField(verbose_name="position")
    modified_at = models.DateTimeField(auto_now=True)


    class Meta:
        unique_together = [
            # no duplicated choice per question
            ("question", "choice"),
            # no duplicated position per question
            ("question", "position")
        ]
        ordering = ("position",)



# Моделька профиля
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    photo = models.ImageField(upload_to='profiles/', blank=True, null=True, verbose_name='Photo')
    phone_number = models.CharField(max_length=30, blank=True, null=True, verbose_name='Phone number')
    about_user = models.CharField(max_length=100, blank=True, null=True, verbose_name='About user')
    points = models.IntegerField(default=0, null=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    # Метод модели для получения фото пользователя
    def get_photo_user(self):
        try:
            return self.photo.url
        except:
            return 'https://thunderbird-mozilla.ru/images/big-images/kak-dobavit-uchetnuyu-zapis-v-mozilla-thunderbird/kak-dobavit-uchetnuyu-zapis-v-mozilla-thunderbird.jpg'



