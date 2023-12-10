from rest_framework import serializers
from play.models import Board

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        extra_kwargs = {'owner': {'write_only': True}}
        fields = ('id', 'name', 'tiles', 'owner')
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data