# Serializery przekształcają dane w JSON, można również 
# zdeklarować które pola mają być zawarte lub nie (include, exclude).
# Dzięki temu, jeśli posiadamy więcej pbiektów w łatwy sposób
# można ograniczyć co będzie wyświetlane

# import klasy serializers oraz własnego modelu utworzonego wcześniej
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        # include - czyli zawarte będą id, autor, tytuł, post, kiedy utworzono
        # exclude - updated_at nie jest zawarte w fields
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post