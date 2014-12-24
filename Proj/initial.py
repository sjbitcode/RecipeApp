#!/usr/bin/env python
import os
import sys
import django
import random

randomUser = lambda: get_user_model().objects.all()[random.randrange(0, get_user_model().objects.count())]
rr = lambda x, y: random.randrange(x, y)

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
  
def makeRecipe(author = None, title = None, slug = None, ingredients = None, method = None, notes = None, tags = None):
    y = rr(1, 10)
    p = rr(1, 15)
    c = rr(15, 50)
    s = Recipe.objects.create(author = author, title = title, ingredients = ingredients, method = method, yieldAmt = y, prepTime = p, cookTime = c, notes = notes)
    for t in tags:
      s.tags.add(t)
    s.save()

## title, slug, ingredients, method, yieldAmt, prepTime, cookTime, notes, author

def main():

  # Make Users.
  Emily = makeUser("emily", "emily@gmail.com", "emily")
  Ramin = makeUser("ramin", "ramin@gmail.com", "ramin")
  Tyler = makeUser("tyler", "tyler@gmail.com", "tyler")
  Bella = makeUser("bella", "bella@gmail.com", "bella")
  Jessica = makeUser("jessica", "jessica@gmail.com", "jessica")
  Freddy = makeUser("freddy", "freddy@gmail.com", "freddy")
  Drogo = get_user_model().objects.create_superuser(username = "drogo", email = "drogo@gmail.com", password = "drogo")
  Harry = get_user_model().objects.create_superuser(username = "harry", email = "harry@gmail.com", password = "harry")
  
  ###################################
  In_r1 = {
    "1":"8 cups finely diced cabbage",
    "2":"1/4 cup diced carrots",
    "3":"2 tablespoons minced onions",
    "4":"1/3 cup granulated sugar",
    "5":"1/2 teaspoon salt",
    "6":"1/8 teaspoon pepper",
    "7":"1/4 cup milk",
    "8":"1/2 cup mayonnaise",
    "9":"1/4 cup buttermilk",
    "10":"1 1/2 tablespoons white vinegar",
    "11":"2 1/2 tablespoons lemon juice"
  }
  Md_r1 = {
    "1":"Cabbage and carrots must be finely diced. (I use fine shredder disc on food processor).",
    "2":"Pour cabbage and carrot mixture into large bowl and stir in minced onions.",
    "3":"Using regular blade on food processor process remaining ingredients until smooth.",
    "4":"Pour over vegetable mixture and mix thoroughly."
  }
  N_r1 = "Cover bowl and refrigerate several hours or overnight before serving."
  makeRecipe(
      title = "KFC Coleslaw",
      ingredients = In_r1,
      method = Md_r1,
      notes = N_r1,
      author = randomUser(),
      tags = ["coleslaw", "salad", "dinner", "lettuce"]
   )
   #--------------------------------------------------------
  
  In_r1 = {
    "1":"1 cup old fashioned rolled oats",
    "2":"2 cups water",
    "3":"sea salt to taste",
    "4":"1/2 tsp cinnamon",
    "5":"1/4 cup raisins",
    "6":"1/4 cup sliced almonds",
    "7":"1 cup skim milk",
    "8":"1 TBS blackstrap molasses",
  }
  Md_r1 = {
    "1":"Bring the water and salt to a boil in a saucepan, then turn the heat to low and add the oats.",
    "2":"Cook for about 5 minutes, stirring regularly so that the oatmeal will not clump together.",
    "3":"Add cinnamon, raisins and almonds, stir, cover the pan and turn off heat.",
    "4":"Let sit for 5 minutes.",
  }
  N_r1 = "Serve with milk and sweetener."
  makeRecipe(
      title = "Five Minute Energizing Oatmeal",
      ingredients = In_r1,
      method = Md_r1,
      notes = N_r1,
      author = randomUser(),
      tags = ["oatmeal", "energy", "food", "yes"]
   )
   #--------------------------------------------------------
    
  In_r1 = {
    "1":"1 cup old fashioned rolled oats",
    "2":"2 cups water",
    "3":"sea salt to taste",
    "4":"1/2 tsp cinnamon",
    "5":"1/4 cup raisins",
    "6":"1/4 cup sliced almonds",
    "7":"1 cup skim milk",
    "8":"1 TBS blackstrap molasses",
  }
  Md_r1 = {
    "1":"Bring the water and salt to a boil in a saucepan, then turn the heat to low and add the oats.",
    "2":"Cook for about 5 minutes, stirring regularly so that the oatmeal will not clump together.",
    "3":"Add cinnamon, raisins and almonds, stir, cover the pan and turn off heat.",
    "4":"Let sit for 5 minutes.",
  }
  N_r1 = "Serve with milk and sweetener."
  makeRecipe(
      title = "Five Minute Energizing Oatmeal",
      ingredients = In_r1,
      method = Md_r1,
      notes = N_r1,
      author = randomUser(),
      tags = ["oatmeal", "energy", "food", "yes"]
   )
   #--------------------------------------------------------
  
  In_r1 = {
    "1":"2 omega-3-rich eggs",
    "2":"1/2 can black beans, drained and mashed",
    "3":"1 TBS extra virgin olive oil",
    "4":"1 tsp lemon juice",
    "5":"sea salt and pepper, to taste",
    "6":"1/4 avocado, sliced",
    "7":"salsa from a jar, to taste",
    "8":"3 TBS grated low-fat cheddar cheese",
    "9":"chopped cilantro, to taste",
  }
  Md_r1 = {
    "1":"Poach eggs.",
    "2":"Heat beans in a skillet while eggs are cooking.",
    "3":"Remove beans from heat and mix in olive oil, lemon juice, salt and pepper Add a pinch of cayenne for spicy beans.",
    "4":"Place beans on plate, top with poached eggs, avocado, salsa, cheese and cilantro",
  }
  N_r1 = "Serve with milk and sweetener."
  makeRecipe(
      title = "Two Minute Huevos Rancheros",
      ingredients = In_r1,
      method = Md_r1,
      notes = N_r1,
      author = randomUser(),
      tags = ["huevos", "ranchero", "mexican", "eggs"]
   )
   #--------------------------------------------------------
    
  In_r1 = {
    "1":"3 eggs warmed in hot water for 5 minutes",
    "2":"pinch salt",
    "3":"1 teaspoon room temperature butter, plus 1/2 teaspoon for finishing omelet",
    "4":"1/2 teaspoon fresh chopped chives",
  }
  Md_r1 = {
    "1":"Crack the warm eggs into a bowl, add salt and blend with a fork. Heat a 10-inch nonstick aluminum pan over medium-high heat. Once the pan is hot, add the butter and brush around the surface of the pan. Pour the eggs         into the center of the pan and stir vigorously with a rubber spatula for 5 seconds.",
    "2":"As soon as a semi-solid mass begins to form, lift the pan and move it around until the excess liquid pours off into the pan. Using your spatula, move it around the edge of the egg mixture to help shape into a round            and loosen the edge. Let the omelet sit in the pan for 10 seconds without touching",
    "3":"Shake the pan to loosen from the pan. Lift up the far edge of the pan and snap it back toward you. Using your spatula, fold over one-third of the omelet. Slide the omelet onto a plate and fold over so that the omelet          is a tri-fold.",
    "4":"Coat with the remaining butter and sprinkle with the chives. Serve immediately.",
  }
  N_r1 = "Add scallions"
  makeRecipe(
      title = "Omelet",
      ingredients = In_r1,
      method = Md_r1,
      notes = N_r1,
      author = randomUser(),
      tags = ["omelet", "tasty", "peppers", "eggs"]
   )
   #--------------------------------------------------------
    
  In_r1 = {
    "1":"11 cup high fiber cereal",
    "2":"1 cup blueberries",
    "3":"2 tsp blackstrap molasses",
    "4":"1/2 cup skim milk or dairy-free milk alternative",
  }
  Md_r1 = {
    "1":"Combine all ingredients and enjoy!",
  }
  N_r1 = ""
  makeRecipe(
      title = "High Fiber Cereal",
      ingredients = In_r1,
      method = Md_r1,
      notes = N_r1,
      author = randomUser(),
      tags = ["cereal", "oats", "fiber", "health"]
   )
  #--------------------------------------------------------

if __name__ == "__main__":
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Proj.settings")
  django.setup()
  from myrecipe.models import Recipe
  from django.contrib.auth import get_user_model
  
  if 'x' in sys.argv[1:]:
    print "Clearing database...\n"
    endall()
  
  main()
