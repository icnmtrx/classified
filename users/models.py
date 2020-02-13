from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from PIL import Image

from .mixins import SlugGenMixin

# Create your models here.
class Profile(SlugGenMixin, models.Model):
    """
    User profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_profile_picture.png', upload_to='profile_pics')
    phone = models.CharField(_("phone"), max_length=30, null=True, blank=True)
    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    registered_at = models.DateTimeField(_('date_registered'), auto_now_add=True)
    last_updated_at = models.DateTimeField(_('date_updated'), auto_now=True)
    slug = models.SlugField(blank=False)

    def save(self, *args, **kwargs):
        self.generate_unique_slug(self)
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


    def allow_add(self):
        """
        Check post limit for a user
        """
        #TODO: move to settings
        limit = 3
        if self.user.item_set.count() <  limit:
            return True
        
        return False

    def __str__(self):
        return f'{self.first_name}' 
        
   