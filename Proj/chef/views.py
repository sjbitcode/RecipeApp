import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.views.generic import View, DetailView, ListView
from django.core.urlresolvers import reverse
from django.views.generic.edit import ProcessFormView
from django.contrib.auth import get_user_model
from braces.views import LoginRequiredMixin
from myrecipe.models import Recipe

User = get_user_model()


class PublicChefView(DetailView):
  """
  View a Chef's public profile.
  """
  model = User
  template_name = "chef/chef.html"
  limit_by = 20
  
  def get_context_data(self, **kwargs):
    """
    Provide additional context data about the Chef (public User).
    """
    context = super(PublicChefView, self).get_context_data(**kwargs)
    usr = context["object"]
    context["recentRecipes"] = usr.recipe_set.all()[:self.limit_by]
    
    # if user has no favorite ingredients, var if false, else true
    hasFavIngred = False if usr.userprofile.favIngredients['favIngredients'].count('') == 3 else True
      
    context["hasFavIngred"] = hasFavIngred
      
    return context
  
  def get_object(self):
    if hasattr(self, 'object'):
      return self.object
    return get_object_or_404(User, username = self.kwargs.get("usrname", ""))
  
  def get(self, request, *args, **kwargs):
    self.object = self.get_object()
    
    if self.object == request.user:
      return HttpResponseRedirect(reverse('chef:dashboard'))
    else:
      return super(PublicChefView, self).get(request, *args, **kwargs)

  
########################################
# Function to see if user has any recipes with any likes
def UserHasLikes(user):
  for r in user.recipe_set.all():
    if r.likes.exists():
      return True
  return False
########################################

class DashboardView(LoginRequiredMixin, DetailView, ProcessFormView):
  """
  Render a User's dashboard.
  """
  model = User
  template_name = "chef/dashboard.html"
  limit_by = 10
  
  def get_context_data(self, **kwargs):
    """
    Provide additional context data about the User.
    """
    context = super(DashboardView, self).get_context_data(**kwargs)
    context["recentRecipes"] = self.request.user.recipe_set.all()[:self.limit_by]
    context["recentLikes"] = self.request.user.favoriter.all()[:self.limit_by]
    if UserHasLikes(self.request.user):
      context["ifLikedByAny"] = True
    context["fav1"] = self.request.user.userprofile.favIngredients["favIngredients"][0]
    context["fav2"] = self.request.user.userprofile.favIngredients["favIngredients"][1]
    context["fav3"] = self.request.user.userprofile.favIngredients["favIngredients"][2]
    return context
  
  def get_object(self):
    return None
  
  
  def post(self, request, *args, **kwargs):
    msg=''
    if request.is_ajax():
      print "request was ajax"
      #import pdb; pdb.set_trace();
      request.user.userprofile.bio = request.POST.get('bio', None)
      print str(request.user.userprofile.bio)
      request.user.userprofile.favIngredients['favIngredients'][0] = request.POST.get('i1', None)
      request.user.userprofile.favIngredients['favIngredients'][1] = request.POST.get('i2', None)
      request.user.userprofile.favIngredients['favIngredients'][2] = request.POST.get('i3', None)
      request.user.userprofile.save()
      print str(request.user.userprofile.favIngredients)
      
      msg = 'Updated properly!!'
      print msg
      return HttpResponse(json.dumps({"msg":msg}), content_type="application/json")
    else:
      msg = 'Did not update properly'
      print msg
      return HttpResponseBadRequest(json.dumps({"msg":msg}), content_type="application/json")
  
class WhoLiked(LoginRequiredMixin, ListView):
  """
  Only an author can see who liked his/her recipe.
  """
  model = Recipe
  template_name= "chef/wholiked.html"
  paginate_by = 10
  page_kwarg = "page"
  
  def get_queryset(self):
    """
    Return list of each recipe with a sublist of users who liked them
    """
    print "I am " + str(self.request.user.username)
    return self.request.user.recipe_set.all()
  
  
class ChefRecipesList(LoginRequiredMixin, ListView):
  """
  Paginated list of User's created Recipes.
  """
  model = Recipe
  template_name = "chef/chefRecipes.html"
  paginate_by = 10
  page_kwarg = "page"
  
  def get_queryset(self):
    """
    Return the list of 'Favorited' Recipes.
    """
    return self.request.user.recipe_set.all()


class ChefFavoritesList(LoginRequiredMixin, ListView):
  """
  Paginated list of User's favorited Recipes.
  """
  model = Recipe
  template_name = "chef/chefFavorites.html"
  paginate_by = 10
  page_kwarg = "page"
  
  def get_queryset(self):
    """
    Return the list of 'Favorited' Recipes.
    """
    return self.request.user.favoriter.all()

