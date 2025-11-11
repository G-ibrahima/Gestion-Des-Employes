"""
Le framework REST fournit deux wrappers que vous pouvez utiliser pour écrire des vues d'API.

Le @api_view décorateur pour travailler avec des vues basées sur des fonctions.
La APIViewclasse permettant de travailler avec des vues basées sur les classes.
Ces wrappers offrent quelques fonctionnalités, comme par exemple s'assurer que vous recevez Requestdes instances dans votre vue et ajouter du contexte aux Responseobjets afin que la négociation de contenu puisse être effectuée.

Les wrappers offrent également des fonctionnalités telles que le renvoi 405 Method Not Allowedde réponses le cas échéant et la gestion des ParseErrorexceptions qui surviennent lors de l'accès request.dataavec des entrées malformées.
"""
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


@api_view(["GET", "POST"])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == "GET":
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET", "PUT", "DELETE"])
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    