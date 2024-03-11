from django.urls import path

from . import views

# Para segurança na aplicação é recomendado adicionar o tipo
# que devemos receber como parametro: str, slug, int
urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),
]
