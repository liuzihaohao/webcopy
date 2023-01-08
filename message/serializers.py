# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import messgaelist,settingslist

class messgaelistdbSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = messgaelist
        fields = ['id','code','typetf','file','text','time']
class settingslistdbSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = settingslist
        fields = ['key','val']