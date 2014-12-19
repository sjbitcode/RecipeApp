from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, Http404, HttpResponseForbidden
from django.views.generic import FormView, CreateView, ListView, DetailView, DeleteView
from django.utils.text import slugify
from django.db.models import Q
from myrecipe.forms import RecipeForm
from myrecipe.models import Recipe
import json, itertools, operator

def gatherQuery(userSearch):
  '''
  Gathers query objects using user's search words
  '''
  searchWordList = userSearch.split(' ')
  recipes = Recipe.objects.all()
  
  q = Q(title__icontains=searchWordList[0]) | Q(ingredString__icontains=searchWordList[0]) | Q(tags__name__in=searchWordList[0])
  for word in searchWordList[1:]:
    q.add((Q(title__icontains=searchWordList[0]) | Q(ingredString__icontains=searchWordList[0]) | Q(tags__name__in=searchWordList[0])), q.connector)

  res = recipes.filter(q).distinct()
  return res

 
"""
userSearchSting = dfifjdlj''
recipeq = gatherQuery(userSearchString)
return Recipe.objects.filter(recipeq).distinct()
"""


class SearchView(ListView):
  """
  Search Recipes by title, tags, and ingredients.
  Results are paginated.
  """
  model = Recipe
  template_name = "myrecipe/searchResults.html"
  context_object_name = "object_list"
  paginate_by = 10
  page_kwarg = "page"
  
  def get_context_data(self, **kwargs):
    context = super(SearchView, self).get_context_data(**kwargs)
    context['recipeQuery'] = self.request.GET.get('recipeQuery', None)
    return context
  
  def get(self, request, *args, **kwargs):
    """
    If no search results, then redirect to search form page.
    """
    self.object_list = self.get_queryset()
    if not self.object_list:
      return HttpResponseRedirect(reverse("myrecipe:searchForm"))
    
    return super(SearchView, self).get(request, *args, **kwargs)
  
  def get_queryset(self):
    """
    Return the list of Recipes.
    """
    #import pdb; pdb.set_trace();
    # If this function has already been called, simply return (exit) from it.
    if hasattr(self, "object_list"):
      return self.object_list
    
    userSearchString = self.request.GET.get("recipeQuery", None)
    
    if not userSearchString:
      return None
    recipeq = gatherQuery(userSearchString)
    
    return recipeq


class DeleteRecipe(DeleteView):
  '''
  Deletes a user's recipe based on slug-name
  '''
  model = Recipe
  template_name = "myrecipe/deleteRecipe.html"
  
  def get_success_url(self):
    return reverse('myrecipe:AllRecipes')
  
  def get_object(self):
    """
    Gets the Recipe to delete.
    If the Recipe does not belong to the (logged-in) User, then 
    raise a 403 error.
    """
    obj = super(DeleteRecipe, self).get_object()
    
    if not obj.author == self.request.user:
      raise Http404
    return obj


class RecipeIMList(object):
  '''
  Mixin to create different context variables for a recipe's ingredients and method fields.
  '''
  def get_context_data(self, **kwargs):
    print "Recipe MIXIN!!!"
    context = super(RecipeIMList, self).get_context_data(**kwargs)
    # making new context key
    context['ingredList'] = sorted(context['object'].ingredients.items())
    context['methodList'] = sorted(context['object'].method.items())
    print context['ingredList']
    return context


# Create your views here.
class RecipeAddView(CreateView):
  form_class = RecipeForm
  model = Recipe
  # This is the 'editing' mode.
  edited = False
  
  def _allowed_methods(self):
    return ['post']
  
  def get_object(self):
    if self.edited:
      return get_object_or_404(self.model, slug = self.slug)
    return super(RecipeAddView, self).get_object()
  
  def post(self, request, *args, **kwargs):
    """
    Handles POST requests, instantiating a form instance with the passed
    POST variables and then checked for validity.
    """
    # If data was POSTed with the 'editing' flag, then override the existing model.
    if request.POST.get("edited", "") == str(True):
      self.edited = True
    
    form_class = self.get_form_class()
    
    if self.edited:
      self.slug = request.POST.get("slug", "")
      self.object = self.get_object()
      if not self.object.author == request.user:
        raise Http404
      form = form_class(request.POST, instance = self.object)
    else:
      form = self.get_form(form_class)
      form.recipeAuthor = request.user
    if form.is_valid():
        return self.form_valid(form)
    else:
        return self.form_invalid(form)
  
  def form_valid(self, form):
    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
    if self.request.is_ajax():
      form.save()
      form.save_m2m()
      return HttpResponse(json.dumps({'success':'was a success!', 'redirectUrl':'/myrecipe/AllRecipes'}), content_type='application/json')
    return super(RecipeAddView, self).form_valid(form)
  
  def form_invalid(self, form):
    if self.request.is_ajax():
      return HttpResponseBadRequest(json.dumps(form.errors), content_type='application/json')
    return super(RecipeAddView, self).form_invalid(form)

class RecipeList(ListView):
  model = Recipe
  template_name = "myrecipe/AllRecipes.html"
  
class SingleRecipe(RecipeIMList, DetailView):
  model = Recipe
  template_name = "myrecipe/SingleRecipe.html"
  
  def get_context_data(self, **kwargs):
    context = super(SingleRecipe, self).get_context_data(**kwargs)
    context["request"] = self.request
    return context
  
class EditRecipe(RecipeIMList, DetailView):
  model = Recipe
  template_name = "myrecipe/EditRecipe.html"
  
  
  

  
  
  

  