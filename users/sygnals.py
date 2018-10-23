from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


#sygnałem będzie User, otrzymującym sygnał będzie receiver, który będzie coś robił Userowi


@receiver(post_save, sender=User)       #(sygnał, nadawca sygnału) kiedy User jest Save'owany to wysyła sygnał
def create_profile(sender, instance, created, **kwargs):   #łapany przez receivera i ten robi profil
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()