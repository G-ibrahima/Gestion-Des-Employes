"""
Notre SnippetSerializerclasse reproduit beaucoup d'informations déjà présentes dans le Snippetmodèle. Il serait préférable de rendre notre code un peu plus concis.

De la même manière que Django fournit à la fois Formdes classes et ModelFormdes classes, le framework REST inclut à la fois Serializerdes classes et ModelSerializerdes classes.
"""

from rest_framework import serializers
from snippets.models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ["id", "title", "code", "linenos", "language", "style"]