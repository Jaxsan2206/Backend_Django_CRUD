from django.http import  Http404
from .models import Pokemon
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PokemonSerializer
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class PokemonList (APIView):
    permission_classes = [IsAuthenticated|ReadOnly]
    def get(self, request, format = None):
        pokemons = Pokemon.objects.all()
        serializer = PokemonSerializer(pokemons, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = PokemonSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class PokemonInd (APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, id):
        try:
            return Pokemon.objects.get(pk=id)
        except Pokemon.DoesNotExist:
            raise Http404

    def get(self, request, id, format = None):
        pokemon = self.get_object(id)
        serializer = PokemonSerializer(pokemon)
        return Response(serializer.data)
    
    def put(self, request,id, format=None):
        pokemon = self.get_object(id)
        serializer = PokemonSerializer(pokemon, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format = None):
        pokemon = self.get_object(id)
        pokemon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
