"""
Utilisation de vues génériques basées sur les classes
Grâce aux classes mixin, nous avons réécrit les vues afin d'utiliser un peu moins de code qu'auparavant, mais nous pouvons aller encore plus loin. REST Framework fournit un ensemble de vues génériques déjà intégrées que nous pouvons utiliser pour alléger views.pydavantage notre module.
"""
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer