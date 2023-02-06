from rest_framework import serializers
from .models import Test

class TestSerializer(serializers.ModelSerializer):
    department=serializers.CharField(label="Enter Department")
    role=serializers.CharField(label="Enter role")
    topic=serializers.CharField(label="Enter Topic")
    question=serializers.CharField(label="Enter question")
    a=serializers.CharField(label="Enter A")
    b=serializers.CharField(label="Enter B")
    c=serializers.CharField(label="Enter C")
    d=serializers.CharField(label="Enter D")


    class Meta:
        model = Test
        fields = ('id', 'department', 'role', 'topic',
              'question', 'a', 'b', 'c','d')
