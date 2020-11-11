from django import forms
# nasz model Post
from .models import Post

# postform - nazwa formularza
# modelForm - formularz
class PostForm(forms.ModelForm):
    # struktura modelu
    class Meta:
        model = Post
        # jakie elementy mają być w formularzu
        fields = ('title', 'text',)