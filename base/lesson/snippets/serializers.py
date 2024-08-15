from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES



class SnippetSerializer(serializers.ModelSerializer):
	"""docstring for SnippetSerializer"""
	class Meta:
		model = Snippet
		fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

	def create(self, validated_data):
		"""
		Create and return a new `snippet` instance, given the validated data.
		"""
		return Snippet.objects.create(**validated_data)

	def update(self, instance, validated_data):
		"""
		Update and return an existing `Snippet` instance, given the validated data.
		"""
		pass
		