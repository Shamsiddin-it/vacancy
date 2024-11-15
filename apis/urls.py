from django.urls import path

from .views import *

urlpatterns = [
    path("vacancy_list/", VacancyAPIView.as_view(), name = "vacancy_list"),
    path("category_list/", CategoryAPIView.as_view(), name = "category_list"),
    path("resume_list/", ResumeAPIView.as_view(), name = "resume_list"),
    path("vacancy_create/", VacancyCreateAPIView.as_view(), name = "vacancy_create"),
    path("vacancy_update/<int:pk>/", VacancyUpdateAPIView.as_view(), name = "vacancy_update"),
    path("vacancy_destroy/<int:pk>/", VacancyDestroyAPIView.as_view(), name = "vacancy_destroy"),
    path("vacancy_rud/<int:pk>/", VacancyRUDAPIView.as_view(), name = "vacancy_rud"),
    path("category_create/", CategoryCreateAPIView.as_view(), name = "category_create"),
    path("category_update/<int:pk>/", CategoryUpdateAPIView.as_view(), name = "category_update"),
    path("category_destroy/<int:pk>/", CategoryDestroyAPIView.as_view(), name = "category_destroy"),
    path("category_rud/<int:pk>/", CategoryRUDAPIView.as_view(), name = "category_rud"),
    path("resume_create/", ResumeCreateAPIView.as_view(), name = "resume_create"),
    path("resume_update/<int:pk>/", ResumeUpdateAPIView.as_view(), name = "resume_update"),
    path("resume_destroy/<int:pk>/", ResumeDestroyAPIView.as_view(), name = "resume_destroy"),
    path("resume_rud/<int:pk>/", ResumeRUDAPIView.as_view(), name = "resume_rud"),
]
