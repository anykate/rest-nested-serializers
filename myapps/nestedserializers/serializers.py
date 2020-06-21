from rest_framework import serializers
from .models import Student, Marks


class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    marks = MarksSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = '__all__'
