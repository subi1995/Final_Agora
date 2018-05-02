# study/forms.py
from django import forms
from .models import Post, Comment, Agora
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content']
		widgets = {
			'title' : forms.TextInput(attrs={'class': 'form-control'}),
		}
class AgoraForm(forms.ModelForm):
	class Meta:
		model = Agora
		fields = ['title', 'content']
		widgets = {
			'title' : forms.TextInput(attrs={'class': 'form-control'}),
		}


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text' : forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': '댓글을 입력해주세요.'}),
        }


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="이메일",
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': '이메일 주소를 입력해주세요'}),
        )
    username = forms.CharField(
        required=True,
        label="ID",
        widget = forms.TextInput(attrs={'class': 'form-control', 'help_text': ''}),
        )

    password1 = forms.CharField(
        required=True,
        label="비밀번호",
        widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '숫자와 문자를 포함해 8자리 이상을 입력해주세요'}),
        )

    password2 = forms.CharField(
        required=True,
        label="비밀번호 확인",
        widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '같은 비밀번호를 다시 입력해주세요.'}),
        )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control', 'help_text': ''}),
        }
