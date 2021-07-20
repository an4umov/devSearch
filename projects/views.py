from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

projectsList = [
    {
        'id': '1',
        'title': 'Ecomerce Website',
        'description': 'Fully functional ecommerce website'
    },
     {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'My portfolio Design'
    },
     {
        'id': '3',
        'title': 'lr.ru',
        'description': 'Fully functional ecommerce CARs website'
    },
]

def projects(request):
    page = 'projects'
    number = 25
    context = {'page' : page, 'number' : number, 'projects': projectsList}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})