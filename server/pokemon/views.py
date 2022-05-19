from django.http import  Http404
from .models import Pokemon
# Create your views here.
import jwt
from rest_framework.exceptions import AuthenticationFailed

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PokemonSerializer

def checkToken (request):
    token = request.COOKIES.get('jwt')
    if not token: 
        raise AuthenticationFailed('Unauthenticated')  
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated')

class PokemonList (APIView):
   
    def get(self, request, format = None):
        pokemons = Pokemon.objects.all()
        serializer = PokemonSerializer(pokemons, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        checkToken(request)
        serializer = PokemonSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class PokemonInd (APIView):
    def get_object(self, id):
        try:
            return Pokemon.objects.get(pk=id)
        except Pokemon.DoesNotExist:
            raise Http404

    def get(self, request, id, format = None):
        checkToken(request)
        pokemon = self.get_object(id)
        serializer = PokemonSerializer(pokemon)
        return Response(serializer.data)
    
    def put(self, request,id, format=None):
        checkToken(request)
        pokemon = self.get_object(id)
        serializer = PokemonSerializer(pokemon, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format = None):
        checkToken(request)
        pokemon = self.get_object(id)
        pokemon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
