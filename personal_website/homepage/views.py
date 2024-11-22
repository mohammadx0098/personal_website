from django.shortcuts import render
from django.views import View
from personal_website.projects.models import Project

class Home(View):
    def get(self, request):
        projects = Project.objects.all().order_by('-category')
        return render(request, "homepage/index.html", context={"projects":projects})
