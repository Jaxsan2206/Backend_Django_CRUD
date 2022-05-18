from django.urls import path 
# from . import views 
from .views import PokemonList, PokemonInd
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', PokemonList.as_view()),
    path('<int:id>', PokemonInd.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# At this point we can also add in the format_suffix_patterns method. All this does is allow users to receive the data in a format they want by adding a suffix such as .json to the endpoint.