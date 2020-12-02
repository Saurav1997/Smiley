from django.forms import ModelForm
from .models import Account

class AccForm (ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
