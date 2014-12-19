from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from myrecipe import views

urlpatterns = patterns('',
  url(r'^addRecipe/$', TemplateView.as_view(template_name="myrecipe/addRecipe.html"), name="addRecipe"),
  url(r'^newRecipeData/$', views.RecipeAddView.as_view(), name="newRecipeData"),
  url(r'^AllRecipes/$', views.RecipeList.as_view(), name="AllRecipes"),
  url(r'^SingleRecipe/(?P<slug>[-\w\d]+)/$', views.SingleRecipe.as_view(), name="singleRecipe"),   
  url(r'^Edit/(?P<slug>[-\w\d]+)/$', views.EditRecipe.as_view(), name="edit"),
  url(r"^search/$", TemplateView.as_view(template_name = "myrecipe/searchForm.html"), name = "searchForm"),
  url(r'^search/results/$', views.SearchView.as_view(), name="search"),
  url(r'^delete/(?P<slug>[-\w\d]+)/$', views.DeleteRecipe.as_view(), name="deleteRecipe"),
  url(r'^like/$', views.ProcessLikes, name="like"),
)