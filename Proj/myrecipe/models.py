from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField
from taggit.managers import TaggableManager
from myrecipe.slug import unique_slugify

# Create your models here.
class Recipe(models.Model):
  title = models.CharField(blank=False, max_length=50)
  ingredients = JSONField(blank=False)
  method = JSONField(blank=False)
  yieldAmt = models.PositiveIntegerField(blank=False)
  prepTime = models.PositiveIntegerField(blank=False)
  cookTime = models.PositiveIntegerField(blank=False)
  notes = models.TextField(blank=True)
  pub_date = models.DateTimeField(auto_now_add = True)
  author = models.ForeignKey(User)
  tags = TaggableManager()
  slug = models.SlugField()
  

  def save(self, **kwargs):
    slug = '%s' % (self.title)
    unique_slugify(self, slug)
    super(Recipe, self).save()

  
  @property
  def totalTime(self):
    return self.prepTime + self.cookTime
  
  def __unicode__(self):
    return self.title
  