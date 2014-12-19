from django.shortcuts import render
from django.views.generic import View, DetailView, ListView
from django.contrib.auth import get_user_model
from braces.views import LoginRequiredMixin
from myrecipe.models import Recipe

User = get_user_model()


class DashboardView(LoginRequiredMixin, DetailView):
  """
  Render a User's dashboard.
  """
  model = User
  template_name = "chef/dashboard.html"
  limit_by = 10
  
  def get_context_data(self, *kwargs):
    """
    Provide additional context data about the User.
    """
    context = super(DashboardView, self).get_context_data(**kwargs)
    context["recentRecipes"] = self.request.user.recipe_set.all()[:self.limit_by]
    context["recentLikes"] = self.request.user.favoriter.all()[:self.limit_by]
    return context
  
  def get_object(self):
    return self.request.user


class ChefRecipesList(LoginRequiredMixin, ListView):
  """
  Paginated list of User's created Recipes.
  """
  model = Recipe
  template_name = "chef/chefRecipes.html"
  paginate_by = 5
  page_kwarg = "page"


class ChefFavoritesList(LoginRequiredMixin, ListView):
  """
  Paginated list of User's favorited Recipes.
  """
  model = Recipe
  template_name = "chef/chefLikes.html"
  paginate_by = 5
  page_kwarg = "page"
  
  def get_queryset(self):
    """
    Return the list of 'Favorited' Recipes.
    """
    return self.request.user.favoriter.all()

