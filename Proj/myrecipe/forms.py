from django.forms import ModelForm
from myrecipe.models import Recipe

class RecipeForm(ModelForm):
  class Meta:
    model = Recipe
    exclude = ['author', 'pub_date']
  
  def clean(self, *args, **kwargs):
    print "I am in clean function of model form\n" 
    print self.cleaned_data
    return self.cleaned_data