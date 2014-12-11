import itertools
from django import forms
from myrecipe.models import Recipe
from django.utils.text import slugify

class RecipeForm(forms.ModelForm):
  class Meta:
    model = Recipe
    exclude = ['author', 'pub_date', 'slug']

  ### clean function for ingredients ###
  def clean_ingredients(self):
    data = self.cleaned_data['ingredients']
    print self.cleaned_data
    
    # Check if all numbers are consecutive.
    #import pdb; pdb.set_trace();
    keys = data.keys()
    keys = [int(k) for k in keys]
    print "keys is: ", keys
    if not keys == range(1, max(keys) + 1):
      raise forms.ValidationError("Non-consecutive ingredients!")
    
    # Check if all dict values are strings.
    val = data.values()
    print "val is: ", val
    for v in val:
      if not isinstance(v, unicode):
        return forms.ValidationError(v, " is not an acceptable type of ingredient!")
    
    return data
  
  ### clean function for methods ###
  def clean_method(self):
    data = self.cleaned_data['method']
    print self.cleaned_data
    
    
    # Check if all numbers are consecutive.
    #import pdb; pdb.set_trace();
    keys = data.keys()
    keys = [int(k) for k in keys]
    if max(keys) < 2:
      raise forms.ValidationError("Must have at least 2 methods for recipe!")
    
    
    print "keys is: ", keys
    if not keys == range(1, max(keys) + 1):
      raise forms.ValidationError("Non-consecutive method steps!")
    
    # Check if all dict values are strings.
    val = data.values()
    print "val is: ", val
    for v in val:
      if not isinstance(v, unicode):
        return forms.ValidationError(v, " is not an acceptable method step!")
    
    return data
  
  def save(self):
    recipe = super(RecipeForm, self).save(commit=False)
      
    recipe.author = self.recipeAuthor

    recipe.slug = orig = slugify(recipe.title)

    for x in itertools.count(1):
      if not Recipe.objects.filter(slug=recipe.slug).exists():
        break
        recipe.slug = '%s-%d' % (orig, x)
          
    recipe.save()
    return recipe
          