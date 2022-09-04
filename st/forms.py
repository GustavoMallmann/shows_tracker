from django.forms import ModelForm
from .models import User_show_info


class User_show_info_form(ModelForm):
    class Meta:
        model = User_show_info
        fields = '__all__'