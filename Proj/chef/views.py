from django.shortcuts import render
from django.views.genric import DetailView, ListView


class DashboardView(DetailView):
  """
  Render a User's dashboard.
  """
  pass


class ChefRecipesList(ListView):
  """
  Paginated list of User's created Recipes.
  """
  pass


class ChefFavoritesList(ListView):
  """
  Paginated list of User's favorited Recipes.
  """
  pass

