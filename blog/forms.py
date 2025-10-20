from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        from .models import Comment
        model = Comment
        exclude = ("post",)
        labels = {
            "user_name": "Name",
            "user_email": "Email",
            "text": "Comment",
        }