from django.db import models
from django.contrib.auth.models import User

# Creating Model for user

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # Adding additional feilds

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self) -> str:
        return f'USER NAME: {self.user.username}'