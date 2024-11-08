from django.shortcuts import render
from .models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.urls import reverse_lazy 
# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class VacancyListView(ListView):
    template_name = "vacancy_list.html"
    model = Vacancy
    context_object_name = "vacancies"

class VacancyCreateView(CreateView):
    template_name = "vacancy_create.html"
    model = Vacancy
    fields = ['name', 'category', 'description', 'duration', 'address', 'salary']
    success_url = reverse_lazy("vacancy_list")

class VacancyUpdateView(UpdateView):
    template_name = "vacancy_update.html"
    model = Vacancy
    fields = ['name', 'category', 'description', 'duration','address', 'salary']
    success_url = reverse_lazy("vacancy_list")

class VacancyDeleteView(DeleteView):
    template_name = "vacancy_delete.html"
    model = Vacancy
    success_url = reverse_lazy("vacancy_list")

class VacancyDetailView(DetailView):
    template_name = "vacancy_detail.html"
    model = Vacancy
    context_object_name = "vacancy"

class CategoryListView(ListView):
    template_name = "category_list.html"
    model = Category
    context_object_name = "categories"

class CategoryCreateView(CreateView):
    template_name = "category_create.html"
    model = Category
    fields = ['name']
    success_url = reverse_lazy("category_list")

class CategoryUpdateView(UpdateView):
    template_name = "category_update.html"
    model = Category
    fields = ['name']
    success_url = reverse_lazy("category_list")

class CategoryDeleteView(DeleteView):
    template_name = "category_delete.html"
    model = Category
    success_url = reverse_lazy("category_list")

class CategoryDetailView(DetailView):
    template_name = "category_detail.html"
    model = Category
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filtered_vacancy_list"] = Vacancy.objects.filter(category = self.kwargs["pk"])
        return context
    
    context_object_name = "category"

class ResumeListView(ListView):
    template_name = "resume_list.html"
    model = Resume
    context_object_name = "resumes"

class ResumeCreateView(CreateView):
    template_name = "resume_create.html"
    model = Resume
    fields = ['vacancy', 'full_name', 'age', 'email', 'description', 'resume']
    success_url = reverse_lazy("resume_list")

class ResumeCreate2View(CreateView):
    template_name = "resume_create_2.html"
    model = Resume
    fields = [ 'full_name', 'age', 'email', 'description', 'resume']
    def form_valid(self, form):
        vacancy = Vacancy.objects.filter(id = self.kwargs["pk"]).first()
        if vacancy:
            form.instance.vacancy = vacancy
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
    
    success_url = reverse_lazy("resume_list")

class ResumeUpdateView(UpdateView):
    template_name = "resume_update.html"
    model = Resume
    fields = ['vacancy', 'full_name', 'age', 'email', 'description', 'resume']
    success_url = reverse_lazy("resume_list")

class ResumeDeleteView(DeleteView):
    template_name = "resume_delete.html"
    model = Resume
    success_url = reverse_lazy("resume_list")

class ResumeDetailView(DetailView):
    template_name = "resume_detail.html"
    model = Resume
    context_object_name = "resume"