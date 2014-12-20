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
  Emily = makeUser("emily", "emily@gmail.com", "emily")
  Ramin = makeUser("ramin", "ramin@gmail.com", "ramin")
  Tyler = makeUser("tyler", "tyler@gmail.com", "tyler")
  Bella = makeUser("bella", "bella@gmail.com", "bella")
  Drogo = get_user_model().objects.create_superuser(username = "drogo", email = "drogo@gmail.com", password = "drogo")
  Harry = get_user_model().objects.create_superuser(username = "harry", email = "harry@gmail.com", password = "harry")
  
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
  ######################################
  In_r6 = {
    "1":"angel hair pasta",
    "2":"spinach",
    "3":"pesto",
    "4":"1 tsp salt",
    "5":"1 tsp black pepper",
    "6":"olive oil",
    "7":"tomator puree"
  }
  Md_r6 = {
    "1":"Boil paste and put aside",
    "2":"Mix in spinach, oil, salt, and black pepper",
    "3":"Pour in oil in pan",
    "4":"Add tomator purree",
    "5":"Mix and serve with cilantro"
  }
  r6 = Recipe.objects.create(title="Spinach Pasta", slug="spinach-pasta", ingredients=In_r6, method=Md_r6, yieldAmt=4, prepTime=6, cookTime=12, author=Emily)
  r6.tags.add("pasta")
  r6.tags.add("spinach")
  r6.tags.add("olive oil")
  r6.tags.add("tomato")
  ######################################
  In_r7 = {
    "1":"couscous",
    "2":"corn",
    "3":"basil",
    "4":"1 tsp salt",
    "5":"1 tsp black pepper",
    "6":"olive oil",
    "7":"3 red peppers"
  }
  Md_r7 = {
    "1":"Stir fry the stuff",
    "2":"Mix basil, oil, salt, red pepper, and black pepper",
    "3":"Pour in oil in pan"
  }
  N_r7 = "Drink some tea after"
  r7 = Recipe.objects.create(title="Iranian Stew", slug="iranian-stew", ingredients=In_r7, method=Md_r7, yieldAmt=5, prepTime=10, cookTime=15, notes=N_r7, author=Ramin)
  r7.tags.add("couscous")
  r7.tags.add("basil")
  r7.tags.add("red pepper")
  ######################################
  In_r8 = {
    "1":"2 chopped kiwi",
    "2":"3 chopped plums",
    "3":"flax seeds 2 tbsp",
    "4":"1 cup greek yogurt plain"
  }
  Md_r8 = {
    "1":"Put all fruit into bowl",
    "2":"Add yogurt",
    "3":"Sprinke flax ontop"
  }
  N_r8 = "You can use any tropical fruits as well"
  r8 = Recipe.objects.create(title="Kiwi Plum Fruit Bowl", slug="kiwi-plum-fruit-bowl", ingredients=In_r8, method=Md_r8, yieldAmt=1, prepTime=8, cookTime=0, author=Harry)
  r8.tags.add("kiwi")
  r8.tags.add("plum")
  r8.tags.add("yogurt")
  r8.tags.add("flax")
  ###################################
  In_r9 = {
    "1":"1 pack hotdog buns",
    "2":"1 chicken hotdogs",
    "4":"sauce",
    "5":"black pepper"
  }
  Md_r9 = {
    "1":"Barbecue hotdogs",
    "2":"Cut hotdog buns in half",
    "3":"Put hotdog in bun",
    "4":"Garnish with mustard"
  }
  N_r9 = "The longer you leave on grill, more smoky flavor"
  r9 = Recipe.objects.create(title="Hotdogs", slug="hotdogs", ingredients=In_r9, method=Md_r9, yieldAmt=5, prepTime=10, cookTime=10, notes=N_r9, author=Drogo)
  r9.tags.add("hotdog")
  r9.tags.add("chicken")
  r9.tags.add("bread")
  ######################################
  
  In_r15 = {
    "1":"One banana",
    "2":"Lots of cinnamon",
  }
  Md_r15 = {
    "1":"Do some stuff.",
    "2":"call Jedi to mix batter.",
    "3":"Retweet",
  }
  r15 = Recipe.objects.create(title="Banana Jedi Cinnamon Tweets", slug="banana-jedi-cinnamon-tweets", ingredients=In_r15, method=Md_r15, yieldAmt=1, prepTime=5, cookTime=5, author=Harry)
  r15.tags.add("wtf")
  r15.tags.add("jedi")
  r15.tags.add("anakin")

######################################
  In_r11 = {
    "1":"One pen",
    "2":"Piece of black paper",
  }
  Md_r11 = {
    "1":"Break pen over the black paper",
    "2":"Light a candle",
    "3":"Drain ink from pen",
  }
  r11 = Recipe.objects.create(title="Pen ritual for prosperity", slug="pen-ritual-for-prosperity", ingredients=In_r11, method=Md_r11, yieldAmt=1, prepTime=5, cookTime=5, author=Drogo)
  r11.tags.add("pen")
  r11.tags.add("ritual")
  r11.tags.add("black")

######################################
  In_r12 = {
    "1":"1 Milk",
    "2":"2 shakes",
    "5":"1 tsp black pepper"
  }
  Md_r12 = {
    "1":"Pour in mixture and cook for 5 minutes",
    "2": "Pour out and drink"
  }
  r12 = Recipe.objects.create(title="Berry blue milk Shake", slug="berry-blue-milk-shake", ingredients=In_r12, method=Md_r12, yieldAmt=1, prepTime=5, cookTime=5, author=Tyler)
  r12.tags.add("smoothie")
  r12.tags.add("milk")
  r12.tags.add("milkshake")
  r12.tags.add("milk shake")

######################################
  In_r13 = {
    "1":"3 chocolate cakes",
    "2":"1 cup happiness",
  }
  Md_r13 = {
    "1":"Break eggs over chocolate cake ",
    "2":"Pour happiness and black pepper",
  }
  r13 = Recipe.objects.create(title="Willy Woka land of Chocolate", slug="willy-wonka-land-of-chocolate", ingredients=In_r13, method=Md_r13, yieldAmt=1, prepTime=5, cookTime=5, author=Ramin)
  r13.tags.add("wonka")
  r13.tags.add("chocolate")
  r13.tags.add("cake")

######################################
  In_r14 = {
    "1":"turkey from super(market)",
    "2":"some nice bread",
    "3":"lots of spicy sauce",
  }
  Md_r14 = {
    "1":"make burger",
    "2":"Mix in spinach, oil, salt, and black pepper",
    "3":"Eat and be happy",
  }
  r14 = Recipe.objects.create(title="Turkey burger", slug="turkey-burger", ingredients=In_r14, method=Md_r14, yieldAmt=1, prepTime=5, cookTime=5, author=Ramin)
  r14.tags.add("eggs")
  r14.tags.add("burger")
  r14.tags.add("turkey")
  r14.tags.add("bread")


if __name__ == "__main__":
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Proj.settings")
  django.setup()
  from myrecipe.models import Recipe
  from django.contrib.auth import get_user_model
  
  if 'x' in sys.argv[1:]:
    print "Clearing database...\n"
    endall()
  
  main()

