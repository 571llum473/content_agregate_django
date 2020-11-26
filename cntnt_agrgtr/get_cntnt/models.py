from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Source(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    rss = models.URLField(max_length=200)
    TECH = 'tech'
    SPORT = 'sport'
    POLITICS = 'politics'
    ENTERTAINMENT = 'entertainment'
    LIFESTYLE = 'lifestyle'
    BUSINESS = 'business'
    SCIENCE = 'science'
    CAT_CHOICES = [
        (TECH, 'Технологии'),
        (SPORT, 'Спорт'),
        (POLITICS, 'Политика'),
        (ENTERTAINMENT, 'Развлечения'),
        (LIFESTYLE, 'Образ жизни'),
        (BUSINESS, 'Бизнес'),
        (SCIENCE, 'Наука')
    ]
    category = models.CharField(max_length=20, choices = CAT_CHOICES, default = LIFESTYLE)
    def __str__(self):
        return self.name

class News(models.Model):
    source = models.ForeignKey(Source, on_delete = models.CASCADE)
    news_text = models.CharField(max_length=200)
    pub_time = models.TimeField('time published',  default=timezone.now)
    snippet = models.CharField(max_length=200, default='Новость недоступна для просмотра')
    url = models.URLField(max_length=200, unique=True)
    def __str__(self):
        return self.news_text

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    love_list = models.ManyToManyField(Source)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
