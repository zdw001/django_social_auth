from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    website = models.CharField(max_length=255, blank=True)
    instagram_username = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username

    # def save_profile(backend, user, response, *args, **kwargs):
    #     if backend.name == 'facebook':
    #         profile = user.get_profile()
    #         if profile is None:
    #             profile = Profile(user_id=user.id)
    #         profile.gender = response.get('gender')
    #         profile.link = response.get('link')
    #         profile.timezone = response.get('timezone')
    #         profile.save()
    #     if backend.name == 'instagram':
    #         profile = user.get_profile()
    #         print(profile)
    #         if profile is None:
    #             profile = Profile(user_id=user.id)
    #         print(response)
    #         profile.gender = response.get('gender')
    #         profile.link = response.get('link')
    #         profile.timezone = response.get('timezone')
    #         profile.save()

    def get_response(user, response, *args, **kwargs):
        profile = user.get_profile()
        resp = response

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()