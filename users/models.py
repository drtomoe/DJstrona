from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):        #dzidziczy po, daje dostęp do pól models.xxField
    user = models.OneToOneField(User, on_delete='models.CASCADE')      #relacja 1-do-1 --> jeden profil ma 1 Usera
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save() #nadpisujemy działalnosć funksji 'save'

        img = Image.open(self.image.path)

        if img.height > 300 or img.width >300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

