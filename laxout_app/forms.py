from django import forms
from .models import Laxout_User

class UserForm(forms.ModelForm):
    class Meta:
        model = Laxout_User
        fields = ["laxout_user_name", "note"] # not  fields = ["laxout_user_name, note"] !


