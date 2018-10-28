from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_shop = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Shop(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ShopOwner = models.CharField(max_length=255)
    ShopName = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    NumOfAds = models.IntegerField()
    Advertisement = models.FileField()
    ProfilePic = models.FileField()

    timestamp = models.DateTimeField()


    def __str__(self):
        return str(self.ShopName)

class Customer(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    followingShops = models.ManyToManyField(Shop, related_name='interested_shops', blank=True)
    timestamp = models.DateTimeField()

    def __str__(self):
        return str(self.user.username)