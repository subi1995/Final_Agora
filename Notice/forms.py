# study/forms.py
from django import forms
from .models import Agora
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AgoraForm(forms.ModelForm):
	class Meta:
		model = Agora
		fields = ['title', 'content']
		widgets = {
			'title' : forms.TextInput(attrs={'class': 'form-control'}),
		}

