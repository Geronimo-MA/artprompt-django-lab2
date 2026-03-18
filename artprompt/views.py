from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse


def index(request):
    return HttpResponse(
        "<h1>ArtPrompt — сайт для художников</h1>"
        "<ul>"
        "<li><a href='/ideas/1/'>Идея по id</a></li>"
        "<li><a href='/ideas/landscape/'>Идея по slug</a></li>"
        "<li><a href='/archive/2023/'>Архив 2023</a></li>"
        "<li><a href='/archive/2025/'>Архив 2025 (404)</a></li>"
        "<li><a href='/search/?style=watercolor&type=idea'>Поиск (GET)</a></li>"
        "<li><a href='/generate/'>Сгенерировать идею (POST)</a></li>"
        "<li><a href='/go-home/'>Redirect</a></li>"
        "</ul>"
    )


def idea_by_id(request, idea_id):
    return HttpResponse(f"<h2>Идея по id</h2><p>idea_id = {idea_id}</p>")


def idea_by_slug(request, idea_slug):
    print("GET данные:", request.GET)

    extra = ""
    if request.GET:
        extra = f"<p>GET: {dict(request.GET)}</p>"

    return HttpResponse(f"<h2>Идея</h2><p>slug = {idea_slug}</p>{extra}")


def archive(request, year):
    if year > 2023:
        raise Http404("Архив недоступен")
    return HttpResponse(f"<h2>Архив</h2><p>year = {year}</p>")


def search(request):
    print("GET данные:", request.GET)

    style = request.GET.get("style", "")
    t = request.GET.get("type", "")
    return HttpResponse(
        "<h2>Поиск (GET)</h2>"
        f"<p>style = {style}</p>"
        f"<p>type = {t}</p>"
    )


@csrf_exempt
def generate(request):
    if request.method == "POST":
        return HttpResponse("<h2>Идея сгенерирована 🎨</h2>")

    return HttpResponse(
        "<h2>Генерация идеи (POST)</h2>"
        "<form method='post'>"
        "<button type='submit'>Сгенерировать</button>"
        "</form>"
    )


def go_home(request):
    return redirect('home')