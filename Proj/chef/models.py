from django.db import models
from django.conf import settings
from jsonfield import JSONField

class UserProfile(models.Model):
  """
  The UserProfile model will hold secondary
  data associated with the User.
  """
  # The User that this object is connected to.
  user = models.OneToOneField(settings.AUTH_USER_MODEL, unique = True, blank = False)
  # Small biography of User.
  bio = models.TextField(max_length = 300, default = "", blank = True)
  favIngredients = JSONField(blank=True, default={"favIngredients":["", "", ""]})
  
  def __unicode__(self):
    return "%s Profile" %(self.user.username)


def createUserProfile(sender, **kwargs):
  """
  Create a UserProfile object each time a new User is created.
  """
  # If 'created' is True...
  if kwargs.get("created", None) and kwargs["created"]:
    # See if 'instance' exists...
    if kwargs.get("instance", None) and kwargs["instance"]:
      bioText = "Hey everyone! I'm " + kwargs["instance"].username + ", and I love to cook!"
      usrprofile, created = UserProfile.objects.get_or_create(user = kwargs["instance"], bio = bioText)

# Connect the signal.
models.signals.post_save.connect(createUserProfile, sender = settings.AUTH_USER_MODEL)
