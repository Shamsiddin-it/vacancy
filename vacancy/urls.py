from django.urls import path
from .views import *

urlpatterns = [
    path("", Home.as_view(), name = "home"),
    path("vacancy_list/", VacancyListView.as_view(), name = "vacancy_list"),
    path("vacancy_create/", VacancyCreateView.as_view(), name = "vacancy_create"),
    path("vacancy_update/<int:pk>/", VacancyUpdateView.as_view(), name = "vacancy_update"),
    path("vacancy_delete/<int:pk>/", VacancyDeleteView.as_view(), name = "vacancy_delete"),
    path("vacancy_detail/<int:pk>/", VacancyDetailView.as_view(), name = "vacancy_detail"),
    path("category_list/", CategoryListView.as_view(), name = "category_list"),
    path("category_create/", CategoryCreateView.as_view(), name = "category_create"),
    path("category_update/<int:pk>/", CategoryUpdateView.as_view(), name = "category_update"),
    path("category_delete/<int:pk>/", CategoryDeleteView.as_view(), name = "category_delete"),
    path("category_detail/<int:pk>/", CategoryDetailView.as_view(), name = "category_detail"),
    path("resume_list/", ResumeListView.as_view(), name = "resume_list"),
    path("resume_create/", ResumeCreateView.as_view(), name = "resume_create"),
    path("resume_update/<int:pk>/", ResumeUpdateView.as_view(), name = "resume_update"),
    path("resume_delete/<int:pk>/", ResumeDeleteView.as_view(), name = "resume_delete"),
    path("resume_detail/<int:pk>/", ResumeDetailView.as_view(), name = "resume_detail"),
]
