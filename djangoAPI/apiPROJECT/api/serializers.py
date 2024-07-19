from dataclasses import field
from statistics import mode
from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    """
        we can convert different data types to native Python
    """
    class Meta:
        model = Course
        fields = '__all__'