from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest 
from django.views.generic.edit import FormView, CreateView
from myrecipe.forms import RecipeForm
from myrecipe.models import Recipe
import json

# Create your views here.
class RecipeForm(CreateView):
  form_class = RecipeForm
  model = Recipe
  
  '''
  def dispatch(self, request, *args, **kwargs):
    if not request.is_ajax():
      return HttpResponseBadRequest(json.dumps({'bad':'only ajax requests allowed'}))
    return super(RecipeForm, self).dispatch(request, *args, **kwargs)
  '''
  
  def _allowed_methods(self):
    return ['post']
  
  def form_valid(self, form):
    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
    if self.request.is_ajax():
      recipe = form.save(commit=False)
      recipe.author = self.request.user
      recipe.save()
      return HttpResponse(json.dumps({'success':'was a success!'}), content_type='application/json')
    return super(RecipeForm, self).form_valid(form)
  
  def form_invalid(self, form):
    if self.request.is_ajax():
      return HttpResponse(json.dumps(form.errors), content_type='application/json')
    return super(RecipeForm, self).form_invalid(form)
  