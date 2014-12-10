from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest 
from django.views.generic.edit import FormView, CreateView
from myrecipe.forms import RecipeForm
from myrecipe.models import Recipe
import json

# Create your views here.
class RecipeForm(CreateView):
  form_class = RecipeForm
  
  def _allowed_methods(self):
    return ['post']
  
  def form_valid(self, form):
    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
    if self.request.is_ajax():
      recipe = form.save(commit=False)
      #recipe.author = self.request.user
      recipe.author = User.objects.get(username='geet')
      recipe.save()
      form.save_m2m()
      return HttpResponse(json.dumps({'success':'was a success!'}), content_type='application/json')
    return super(RecipeForm, self).form_valid(form)
  
  def form_invalid(self, form):
    if self.request.is_ajax():
      return HttpResponse(json.dumps(form.errors), content_type='application/json')
    return super(RecipeForm, self).form_invalid(form)
  