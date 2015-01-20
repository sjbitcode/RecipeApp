from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from myrecipe.models import Recipe

# Create your tests here.
class RecipeTest(TestCase):
  def setup(self):
    pass
  
  def createUser(self, name, email, password):
    return User.objects.create_user(name, email, password)
  
  def test_recipe_name(self):
    Recipe.objects.create(title="Smoothie", author=self.createUser("Sammy", "sammy@email.com", "top_secret"), ingredients={"1":"milk", "2":"banana"}, method={"1":"pour milk in blender", "2":"put banana in blender", "3":"blend"}, 
                         yieldAmt=5, prepTime=4, cookTime=5)
    recipename = Recipe.objects.get(title="Smoothie").title
    self.assertEqual(recipename, "Smoothie")