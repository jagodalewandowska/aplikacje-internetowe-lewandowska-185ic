from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
# import serializera i modelu przepis
from recipebook.models import Recipe
from recipebook.serializers import RecipeSerializer

# aby api_view dzialalo
from rest_framework.decorators import api_view


# GET - lista przepisów, POST - dodaj nowy przepis, DELETE - usuń przepisy
@api_view(['GET', 'POST', 'DELETE'])
def recipe_list(request):

    # ----------- dla metody get ----------------------------------------
    if request.method == 'GET':
        # zebranie wszystkich obiektów przepis
        recipes = Recipe.objects.all()        
        # pobierz tytuł
        title = request.GET.get('title', None)
        # jeśli istnieje, filtruj po tytule
        if title is not None:
            recipes = recipes.filter(title__icontains=title)
        # wyświetl tylko te elementy wymienione w serializerze
        recipe_serializer = RecipeSerializer(recipes, many=True)
        return JsonResponse(recipe_serializer.data, safe=False)

    # ----------- dla metody post ----------------------------------------
    elif request.method == 'POST':      
        # utworzenie zmiennej przechowywującej zapytanie
        # oraz serializera dla tych danych  
        recipe_data = JSONParser().parse(request)
        recipe_serializer = RecipeSerializer(data=recipe_data)
        # jeśli jest dobrze wpisane, zapisuje
        if recipe_serializer.is_valid():
            recipe_serializer.save()
            # zwracanie nowego przepisu ze statusem http 201 created
            return JsonResponse(recipe_serializer.data, status=status.HTTP_201_CREATED) 
        # jeśli zły wpis, to zwraca błąd oraz bad requests
        return JsonResponse(recipe_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ----------- dla metody delete --------------------------------------
    elif request.method == 'DELETE': 
        count = Recipe.objects.all().delete()
        return JsonResponse({'message': '{} Recipes were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def recipe_detail(request, pk):
    # odszukiwanie przepisu po id
    try: 
        # utworzenie zmiennej recipe, dla której porównywane jest id
        recipe = Recipe.objects.get(pk=pk) 
    # wyłapanie kiedy nie istnieje
    except Recipe.DoesNotExist: 
        # zwracanie informacji, że przepis nie istnieje
        return JsonResponse({'message': 'The recipe does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    # metoda get, do wyświetlenia odnalezionego przepisu
    if request.method == 'GET': 
        recipe_serializer = RecipeSerializer(recipe) 
        # zwracanie z użyciem serializera
        return JsonResponse(recipe_serializer.data) 
 
    # dla metody put
    elif request.method == 'PUT': 
            recipe_data = JSONParser().parse(request) 
            recipe_serializer = RecipeSerializer(recipe, data=recipe_data) 
            # jeśli serializer jest prawidłowy
            if recipe_serializer.is_valid(): 
                recipe_serializer.save() 
                return JsonResponse(recipe_serializer.data) 
            # jeśli złe zapytanie
            return JsonResponse(recipe_serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
            
    # usuwanie przepisu
    elif request.method == 'DELETE': 
        recipe.delete() 
        return JsonResponse({'message': 'Recipe was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

# GET - wyświetl wszystkie dodane przepisy
@api_view(['GET'])
def recipe_list_published(request):
    recipes = Recipe.objects.filter(published=True)
        
    if request.method == 'GET': 
        recipe_serializer = RecipeSerializer(recipes, many=True)
        return JsonResponse(recipe_serializer.data, safe=False)