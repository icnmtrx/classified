"""
Docstring
"""
from django.urls import reverse
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from unidecode import unidecode
from users.models import Profile
from django.utils.crypto import get_random_string
from django.utils import translation

user_language = 'ru'
translation.activate(user_language)
#request.session[translation.LANGUAGE_SESSION_KEY] = user_language

class Region(models.Model):
    """
    Region
    """
    slug = models.SlugField(blank=False, unique=True)
    title = models.CharField(_('region'), max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('region')
        verbose_name_plural = _('regions')


class Category(models.Model):
    """
    Category
    """
    slug = models.SlugField(blank=False, unique=True)
    title = models.CharField(_('category'), max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')




class ClassifiedAd(models.Model):
    slug = models.SlugField(max_length=100, blank=False, unique=True)

    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    header = models.CharField(_('header'), max_length=100)
    body = models.TextField(_('body'), max_length=1000)
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2)
    date_posted = models.DateTimeField(_('date_posted'), auto_now_add=True)
    date_updated = models.DateTimeField(_('date_updated'), auto_now=True)

    #TODO: replace one image to image
    image = models.ImageField(default='default_missing.png', upload_to='images')

    active = models.BooleanField(_('active'), default=True)
    moderation = models.BooleanField(_('moderation'), default=False)

    def __str__(self):
        return self.header

    class Meta:
        ordering = ('-date_updated',)
        verbose_name = _('advert')
        verbose_name_plural = _('adverts')

    def get_contact_phone(self):
        return self.author.phone

    def save(self, *args, **kwargs):
        if not self.slug:
            # TODO: fix random to prevent rare but possible collisions here
            self.slug = slugify(unidecode(self.header)) + '-' + \
                        get_random_string(length=5, allowed_chars='0123456789')
        
        super(ClassifiedAd, self).save(args, kwargs)

    def get_absolute_url(self):
        return reverse('adv-detail', kwargs={'adv':self.slug})

