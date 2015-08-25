from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    nickname = models.CharField(max_length=25)
    likes_toblerone = models.BooleanField(default=False)

    # Usage:
    # nickname = request.user.profile.nickname

    def __str__(self):
        return self.nickname

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
