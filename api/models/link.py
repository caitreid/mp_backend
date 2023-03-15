from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Link(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  name = models.CharField(max_length=100)
  url = models.CharField(max_length=300)
  visible =  models.BooleanField()
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"'{self.owner}' has a link '{self.name}'."

  def as_dict(self):
    """Returns dictionary version of Link models"""
    return {
        'id': self.id,
        'name': self.name,
        'url': self.url,
        'visible': self.visible,
        'owner': self.owner
    }
