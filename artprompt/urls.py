from django.urls import path, register_converter
from . import views
from .converters import FourDigitYearConverter

register_converter(FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),

    # динамические URL
    path('ideas/<int:idea_id>/', views.idea_by_id, name='idea_id'),
    path('ideas/<slug:idea_slug>/', views.idea_by_slug, name='idea_slug'),

    # конвертер
    path('archive/<year4:year>/', views.archive, name='archive'),

    # GET
    path('search/', views.search, name='search'),

    # POST
    path('generate/', views.generate, name='generate'),

    # redirect
    path('go-home/', views.go_home, name='go_home'),
]