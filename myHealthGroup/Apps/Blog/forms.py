from django import forms
from django.forms import ModelForm, Textarea
from myHealthGroup.Apps.Blog.models import Post

class Post_Form(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('Title','Category','Description')
