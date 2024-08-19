from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
	"""docstring for SnippetSerializer"""
	owner = serializers.ReadOnlyFeild(source='owner.username')
	class Meta:
		model = Snippet
		fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner'] #optimisation, problem aalways need instance of object 
																		 #n+1 problem, happens with lots of relationships


class UserSerializer(serializers.ModelSerializer):
	snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

	class Meta:
		model = User 
		fields = ['id', 'username', 'snippets']