from rest_framework import serializers
from .models import Student

class StudentsSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=50)

    '''Implementation for the Create method API in Serializer File'''
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    '''Implementing the update method '''
    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
