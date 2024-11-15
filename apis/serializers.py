from rest_framework import serializers
from vacancy.models import *

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'

