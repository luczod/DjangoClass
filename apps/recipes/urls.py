from django.urls import path
# from recipes.views import contato, home, sobre
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipeListViewHome.as_view(), name="home"),  # Home
    path('recipes/search/',
         views.RecipeListViewSearch.as_view(), name="search"),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name="recipe"),
    path('recipes/category/<int:id>/',
         views.RecipeListViewCategory.as_view(), name="category"),
]
