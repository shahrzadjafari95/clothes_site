from django import forms
from .models import Comment, Newsletter


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']


class NewsletterForm(forms.ModelForm):
