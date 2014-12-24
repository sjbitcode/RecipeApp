import itertools
from django import forms
from myrecipe.models import Recipe
from django.utils.text import slugify

MAX_TAGS = 12

class RecipeForm(forms.ModelForm):
  title = forms.CharField(error_messages = {"required": "You must enter a title."})
  yieldAmt = forms.CharField(error_messages = {"required": "A recipe must have a Yield Amount."})
  cookTime = forms.CharField(error_messages = {"required": "A Recipe must have a Cook Time."})
  prepTime = forms.CharField(error_messages = {"required": "A recipe must have a Preparation time amount."})
  
  class Meta:
    model = Recipe
    exclude = ['author', 'pub_date', 'slug', 'ingredString', 'fav']

  ### clean function for ingredients ###
  def clean_ingredients(self):
    data = self.cleaned_data['ingredients']
    print self.cleaned_data
    
    # Check if all numbers are consecutive.
    #import pdb; pdb.set_trace();
    keys = sorted(data.keys())
    keys = [int(k) for k in keys]
    for k in keys:
      print k
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
    keys = sorted(data.keys())
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
  
  ### clean function for tags ###
  def clean_tags(self):
    print "in tags clean function now!"
    data = self.cleaned_data.get("tags", None)
    
     # Do the number of tags exceed the maximum?
    if len(data) > MAX_TAGS:
      raise forms.ValidationError("Only allowed %s tags per Recipe." %(MAX_TAGS))
    
    # Turn all tags into lower case.
    data = [tag.lower() for tag in data]
    
    return data
    
  
  def save(self):
    print "In save function now!"
    recipe = super(RecipeForm, self).save(commit=False)
    
    if hasattr(self, "recipeAuthor"):
      recipe.author = self.recipeAuthor

    '''
    recipe.slug = orig = slugify(recipe.title)

    for x in itertools.count(1):
      if not Recipe.objects.filter(slug=recipe.slug).exists():
        break
        recipe.slug = '%s-%d' % (orig, x)
        
    print str(recipe.slug)
    '''
          
    recipe.save()
    return recipe
          