from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from myrecipe import views

urlpatterns = patterns('',
                       
  ### Adds a new recipe. ###                     
  url(r'^add/$', views.NewRecipeView.as_view(template_name="myrecipe/addRecipe.html"), name="addRecipe"),
                       
  ### Ajax view for adding recipe. ###
  url(r'^new/$', views.RecipeAddView.as_view(), name="newRecipeData"),
                       
  ### Display list of all recipes. ###
  url(r'^all/$', views.RecipeList.as_view(), name="AllRecipes"),
                       
  ### Displays detailed view of a single recipe. ###
  url(r'^recipe/(?P<slug>[-\w\d]+)/$', views.SingleRecipe.as_view(), name="singleRecipe"),
                       
  ### Edit an existing recipe. ###
  url(r'^edit/(?P<slug>[-\w\d]+)/$', views.EditRecipe.as_view(), name="edit"),
                       
  ### Modify an existing recipe i.e. Edit or Delete ###
  url(r'^modify/$', views.Modify.as_view(), name="modify"),
                       
  ### Search for a recipe. ###
  url(r"^search/$", TemplateView.as_view(template_name = "myrecipe/searchForm.html"), name = "searchForm"),
                       
  ### Displays results of a search query. ###
  url(r'^search/results/$', views.SearchView.as_view(), name="search"),
                       
  ### Landing page for a search with no results. ### 
  url(r'^search/noresults/$', TemplateView.as_view(template_name = "myrecipe/noResults.html"), name="noResults"),
                       
  ### Deletes an existing recipe. ###
  url(r'^delete/(?P<slug>[-\w\d]+)/$', views.DeleteRecipe.as_view(), name="deleteRecipe"),
                       
  ### View to like a recipe. ###
  url(r'^like/$', views.ProcessLikes, name="like"),
                       
  ### Testing Python Social Auth ###
  url(r'^test$', TemplateView.as_view(template_name = "myrecipe/socialauth.html"), name="socialAuth"),
  
  ### Index page ###
  url(r'^/?$',  TemplateView.as_view(template_name = "myrecipe/index.html"), name="index"),
                                 
  ### BASE HTML PAGE ###
  url(r'^base?$',  TemplateView.as_view(template_name = "myrecipe/_base.html"), name="base"),                   
                       
)