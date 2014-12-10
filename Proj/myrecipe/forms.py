from django import forms
from myrecipe.models import Recipe

class RecipeForm(forms.ModelForm):
  class Meta:
    model = Recipe
    exclude = ['author', 'pub_date']

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