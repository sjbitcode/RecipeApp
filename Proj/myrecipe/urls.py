from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from myrecipe import views

urlpatterns = patterns('',
  url(r'^addRecipe/$', TemplateView.as_view(template_name="myrecipe/addRecipe.html"), name="addRecipe"),
  url(r'^newRecipeData/$', views.RecipeForm.as_view(), name="newRecipeData"),
)