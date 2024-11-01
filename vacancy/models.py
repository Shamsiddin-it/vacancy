from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField( max_length=50)
    def __str__(self):
        return self.name


class Vacancy(models.Model):
    name = models.CharField( max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    duration = models.CharField( max_length=50)
    address = models.CharField( max_length=200)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    def __str__(self):
        return self.name
    
class Resume(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    full_name = models.CharField( max_length=50)
    age = models.IntegerField()
    email = models.EmailField(max_length=254)
    description = models.TextField()
    resume = models.FileField( upload_to="static/resume/files", max_length=100)
    def __str__(self):
        return self.full_name


    