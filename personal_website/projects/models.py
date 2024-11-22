from django.db import models

class Project(models.Model):

    class CategoryChoice(models.TextChoices):
        Web = "W", "web development"
        Security = "S", "security"
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    category = models.CharField(max_length=1, choices=CategoryChoice.choices)
    link = models.CharField(max_length=150)
    image = models.ImageField(upload_to="projects")


    def __str__(self):
        return self.title
