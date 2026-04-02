from django.urls import path, register_converter
from . import views
from .converters import FourDigitYearConverter

register_converter(FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('categories/', views.categories, name='categories'),
    path('ideas/<int:idea_id>/', views.idea_by_id, name='idea_id'),
    path('ideas/<slug:idea_slug>/', views.idea_by_slug, name='idea_slug'),
    path('archive/<year4:year>/', views.archive, name='archive'),
    path('search/', views.search, name='search'),
    path('generate/', views.generate, name='generate'),
    path('go-home/', views.go_home, name='go_home'),

]