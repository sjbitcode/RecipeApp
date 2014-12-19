from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',

    url(r'^dashboard/$', views.DashboardView.as_view(), name = "dashboard"),
    url(r'^dashboard/recipes/$', views.ChefRecipesList.as_view(), name = "chefRecipes"),
    url(r'^dashboard/favorites/$', views.ChefFavoritesList.as_view(), name = "chefFavorites"),
)
