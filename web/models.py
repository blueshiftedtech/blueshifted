from django.db import models
from django.forms import ModelForm

# Create your models here.
class WebsiteEmail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=4000)


class WebsiteEmailForm(ModelForm):
    class Meta:
        model = WebsiteEmail
        fields = ['name', 'email', 'message']
