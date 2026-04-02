from django.http import Http404
from django.shortcuts import redirect, render


def index(request):
    data = {
        "title": "ArtPrompt — сайт для художников",
        "description": "Главная страница проекта, оформленная через шаблон Django.",
    }
    return render(request, "artprompt/index.html", data)


def about(request):
    data = {
        "title": "О сайте ArtPrompt",
        "content": "ArtPrompt — учебный Django-проект для художников. На сайте демонстрируется работа шаблонов, маршрутов и обработки запросов.",
    }
    return render(request, "artprompt/about.html", data)


def categories(request):
    data = {
        "title": "Категории идей",
        "categories": [
            "Пейзаж",
            "Портрет",
            "Абстракция",
            "Акварель",
            "Цифровой арт",
            "Натюрморт",
        ],
    }
    return render(request, "artprompt/categories.html", data)


def idea_by_id(request, idea_id):
    return render(request, "artprompt/idea_id.html", {"idea_id": idea_id})


def idea_by_slug(request, idea_slug):
    return render(
        request,
        "artprompt/idea_slug.html",
        {
            "idea_slug": idea_slug,
            "get_params": request.GET.dict(),
        },
    )


def archive(request, year):
    if year > 2023:
        raise Http404("Архив недоступен")
    return render(request, "artprompt/archive.html", {"year": year})


def search(request):
    style = request.GET.get("style", "")
    idea_type = request.GET.get("type", "")
    return render(
        request,
        "artprompt/search.html",
        {
            "style": style,
            "type": idea_type,
        },
    )


def generate(request):
    if request.method == "POST":
        return render(request, "artprompt/generate.html", {"generated": True})

    return render(request, "artprompt/generate.html", {"generated": False})


def go_home(request):
    return redirect("home")