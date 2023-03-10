from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Profile(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  username = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  bio = models.CharField(max_length=250)
  visible =  models.BooleanField()
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The user '{self.owner}' has a username '{self.username}'."

  def as_dict(self):
    """Returns dictionary version of Profile models"""
    return {
        'id': self.id,
        'username': self.username,
        'title': self.title,
        'bio': self.bio,
        'visible': self.visible,
        'owner': self.owner
    }
