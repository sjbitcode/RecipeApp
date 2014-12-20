from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    
    url(r"^chef/(?P<usrname>.*)/$", views.PublicChefView.as_view(), name = "chef"),
    url(r'^dashboard/$', views.DashboardView.as_view(), name = "dashboard"),
    url(r'^dashboard/recipes/$', views.ChefRecipesList.as_view(), name = "chefRecipes"),
    url(r'^dashboard/favorites/$', views.ChefFavoritesList.as_view(), name = "chefFavorites"),
    url(r'^dashboard/recipes/wholiked/$', views.WhoLiked.as_view(), name="wholiked"),
)
