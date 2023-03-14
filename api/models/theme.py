from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Theme(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/

  background_color = models.CharField(max_length=100)
  button_style = models.CharField(max_length=100)
  button_bg_color = models.CharField(max_length=100)
  button_font_color = models.CharField(max_length=100)
  shadow_color = models.CharField(max_length=100)
  font_color = models.CharField(max_length=100)
  profile = models.ForeignKey(
    'Profile',
    on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The profile '{self.profile}' has a bg color of {self.background_color}."

  def as_dict(self):
    """Returns dictionary version of Theme models"""
    return {
        'id': self.id,
        'background_color' : self.background_color,
        'button_style' : self.button_style,
        'button_bg_color' : self.button_bg_color,
        'button_font_color' : self.button_font_color,
        'shadow_color' : self.shadow_color,
        'font_color' : self.font_color,
        'profile' : self.profile
    }
