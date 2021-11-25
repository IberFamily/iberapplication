from django.db.models import fields
from django.db.models.base import Model
from django.forms import forms
from django.forms import ModelForm

from customermsg.models import messages

class sendUsMessage(ModelForm):
   class Meta:
      ordering = ['-created_at']
      model = messages
      fields = '__all__'



