#!/usr/bin/env python
import os
import sys
import django

def endall():
  # Delete Snippets.
  for obj in Recipe.objects.all():
    obj.delete()
  # Delete Users.
  for obj in get_user_model().objects.all():
    obj.delete()

def makeUser(n, e, p):
  try:
    usr = get_user_model().objects.get(username = n)
    return usr
  except get_user_model().DoesNotExist:
    return get_user_model().objects.create_user(username = n, email = e, password = p)
  

def main():

  # Make Users.
  Harry = makeUser("harry", "harry@gmail.com", "harry")
  Emily = makeUser("emily", "emily@gmail.com", "emily")
  Ramin = makeUser("ramin", "ramin@gmail.com", "ramin")
  Tyler = makeUser("tyler", "tyler@gmail.com", "tyler")
  Bella = makeUser("bella", "bella@gmail.com", "bella")
  Drogo = get_user_model().objects.create_superuser(username = "drogo", email = "drogo@gmail.com", password = "drogo")
  
  ###################################
  In_r1 = {
    "1":"chopped chicken",
    "2":"1 cup baby tomatoes",
    "3":"3 cups greens",
    "4":"2 tbsp olive oil"
  }
  Md_r1 = {
    "1":"Wash greens",
    "2":"Cut tomatoes in small pieces",
    "3":"Combine all ingredients in bowl"
  }
  N_r1 = "Add sprinkle of salt for added flavor"
  r1 = Recipe.objects.create(title="Greek Salad", slug="greek-salad", ingredients=In_r1, method=Md_r1, yieldAmt=4, prepTime=10, cookTime=5, notes=N_r1, author=Harry)
  r1.tags.add("chicken")
  r1.tags.add("salad")
  r1.tags.add("healthy")
  r1.tags.add("greens")
  ######################################
  In_r2 = {
    "1":"3 cups flour",
    "2":"2 cups milk",
    "3":"3 sticks butter",
    "4":"1 cup cocoa powder",
    "5":"1 1/2 cup sugar",
    "6":"2 tsp baking powder",
    "7":"1 tsp baking soda",
    "8":"3 eggs"
  }
  Md_r2 = {
    "1":"Combine dry ingredients",
    "2":"Mix wet ingredients with dry ingredients",
    "3":"Combine all ingredients in bowl",
    "4":"Pour into greased tin",
    "5":"Bake on 350 degrees for 45 minutes"
  }
  N_r2 = "Add chocolate chips if desired"
  r2 = Recipe.objects.create(title="Chocolate cake", slug="chocolate-cake", ingredients=In_r2, method=Md_r2, yieldAmt=8, prepTime=20, cookTime=45, notes=N_r2, author=Emily)
  r2.tags.add("chocolate")
  r2.tags.add("baked")
  r2.tags.add("dessert")
  r2.tags.add("cake")
  ######################################
  In_r3 = {
    "1":"2 cups flour",
    "2":"1 cups milk",
    "3":"1 1/2 sticks butter",
    "4":"1 1/2 cup sugar",
    "5":"1 tsp baking powder",
    "6":"1 1/2 tsp baking soda",
    "7":"2 eggs",
    "8":"2 tsp cinammon"
  }
  Md_r3 = {
    "1":"Mix flour and milk",
    "2":"Beat eggs",
    "3":"Combine dry and wet ingredients",
    "4":"Heat pans, and grease, and cook"
  }
  N_r3 = "Add chocolate chips, nuts, or raisins if desired"
  r3 = Recipe.objects.create(title="Fluffy Pancakes", slug="fluffy-pancakes", ingredients=In_r3, method=Md_r3, yieldAmt=16, prepTime=18, cookTime=15, notes=N_r3, author=Ramin)
  r3.tags.add("pancakes")
  r3.tags.add("breakfast")
  ######################################
  In_r4 = {
    "1":"2 cups oatmeal",
    "2":"1 cup milk",
    "3":"1 tsp sugar",
    "4":"1 tsp cinammon"
  }
  Md_r4 = {
    "1":"Warm milk",
    "2":"Add oats",
    "3":"Combine sugar and cinammon"
  }
  N_r4 = "I like to add an apple in mine, making it an even healthier breakfast"
  r4 = Recipe.objects.create(title="Oatmeal", slug="oatmeal", ingredients=In_r4, method=Md_r4, yieldAmt=1, prepTime=5, cookTime=5, notes=N_r4, author=Tyler)
  r4.tags.add("oatmeal")
  r4.tags.add("breakfast")
  r4.tags.add("healthy")
  ######################################
  In_r5 = {
    "1":"3 eggs",
    "2":"1 cup spinach",
    "3":"2 tbsp oil",
    "4":"1 tsp salt",
    "5":"1 tsp black pepper"
  }
  Md_r5 = {
    "1":"Break eggs",
    "2":"Mix in spinach, oil, salt, and black pepper",
    "3":"Pour in oil in pan",
    "4":"Pour in mixture and cook for 5 minutes"
  }
  r5 = Recipe.objects.create(title="Spinach Omlet", slug="spinach-omlet", ingredients=In_r5, method=Md_r5, yieldAmt=1, prepTime=5, cookTime=5, author=Tyler)
  r5.tags.add("eggs")
  r5.tags.add("breakfast")
  r5.tags.add("healthy")
  


if __name__ == "__main__":
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Proj.settings")
  django.setup()
  from myrecipe.models import Recipe
  from django.contrib.auth import get_user_model
  
  if 'x' in sys.argv[1:]:
    print "Clearing database...\n"
    endall()
  
  main()

