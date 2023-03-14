from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Link(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  title = models.CharField(max_length=300)
  url = models.CharField(max_length=300)
  visible =  models.BooleanField()
  order = models.IntegerField()
  profile = models.ForeignKey(
    'Profile',
    on_delete=models.CASCADE
  )


  def __str__(self):
    # This must return a string
    return f"Link: '{self.title}' with url '{self.url} on '{self.profile}'."

  def as_dict(self):
    """Returns dictionary version of Profile models"""
    return {
        'id': self.id,
        'title': self.title,
        'url': self.url,
        'visible': self.visible,
        'order': self.order,
        'profile': self.profile
    }
