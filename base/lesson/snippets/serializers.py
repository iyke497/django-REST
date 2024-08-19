from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
	"""docstring for SnippetSerializer"""
	owner = serializers.ReadOnlyField(source='owner.username')
	highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
	
	class Meta:
		model = Snippet
		fields = ['url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style'] #optimisation, problem aalways need instance of object 
																		 #n+1 problem, happens with lots of relationships


class UserSerializer(serializers.ModelSerializer):
	snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

	class Meta:
		model = User 
		fields = ['url', 'id', 'username', 'snippets']