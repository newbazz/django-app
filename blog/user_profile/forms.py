from django import forms
from . import models

class User_Profile(forms.ModelForm):
	class Meta:
		model = models.User_Profile
		fields = ['sex', 'body']