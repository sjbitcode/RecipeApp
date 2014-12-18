from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest, Http404 
from django.views.generic.edit import FormView, CreateView, ListView
from django.utils.text import slugify
from django.views.generic import ListView, DetailView
from myrecipe.forms import RecipeForm
from myrecipe.models import Recipe
import json, itertools

class Search(ListView):
  


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
  
  
class EditRecipe(RecipeIMList, DetailView):
  model = Recipe
  template_name = "myrecipe/EditRecipe.html"
  
  
  

  
  
  

  