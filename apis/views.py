from rest_framework import generics 
from vacancy.models import *
from .serializers import *

class VacancyAPIView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class VacancyCreateAPIView(generics.CreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class VacancyUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class VacancyDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class VacancyRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ResumeAPIView(generics.ListAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class ResumeCreateAPIView(generics.CreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class ResumeUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class ResumeDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class ResumeRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
