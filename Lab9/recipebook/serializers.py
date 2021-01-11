from rest_framework import serializers 
from recipebook.models import Recipe

# ten serializer dziedziczy z rest_framework.serializers.ModelSerializer,
# defniuje co będzie wyświetlane na stronie
class RecipeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Recipe
        fields = ('id',
                  'title',
                  'description',
                  'published')