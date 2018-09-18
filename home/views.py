from django.shortcuts import render

# python manage.py inspectdb t_film  >models.py
from home.models import Film


def index(request):
    films = Film.objects.all().values('id', 'image', 'name', 'type_name', 'on_decade')
    return render(request, 'index.html', locals())


def detail(request, id):
    film = Film.objects.filter(id=id).values('name', 'image', 'type_name', 'status', 'on_decade', 'update_time', 'plot')
    return render(request, 'detail.html', locals())
