from django import forms
# nasz model Post
from .models import Post

# postform - nazwa formularza
# modelForm - formularz
class PostForm(forms.ModelForm):
    #class Meta przekazujemy informacje o tym jaki model powinien
    #Byc wykorzystany do stworzenia formularza czyli Post
    class Meta:
        model = Post
        # Wybór które elementy mają być w formularzu
        fields = ('title', 'text',)