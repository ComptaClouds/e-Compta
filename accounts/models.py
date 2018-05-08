from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


#def upload_location(instance, filname):
 #   filebase, extension =filename.split(".")
  #  return "%s/%s.%s" %(instance.id, instance.id, filename)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    raison_social = models.CharField(blank=True, null=True, max_length=255)
    logo = models.FileField(upload_to="logo", null=True, blank=True)
    contact = models.IntegerField(default=0)
    activation_key = models.CharField(max_length=255, default=1)
    email = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username



@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()


@property
def photo_url(self):
    if self.logo and hasattr(self.logo, 'url'):
        return self.logo.url