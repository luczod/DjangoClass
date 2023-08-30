from django.urls import path
# from recipes.views import contato, home, sobre
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipeListViewHome.as_view(), name="home"),  # Home
    path(
        'recipes/api/v1/',
        views.RecipeListViewHomeApi.as_view(),
        name="recipes_api_v1",
    ),
    path('recipes/search/',
         views.RecipeListViewSearch.as_view(), name="search"),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name="recipe"),
    path('recipes/api/v1/<int:pk>/',
         views.RecipeDetailAPI.as_view(),
         name="recipes_api_pk",
         ),
    path('recipes/category/<int:id>/',
         views.RecipeListViewCategory.as_view(), name="category"),
]
