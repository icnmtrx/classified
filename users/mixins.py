from django.db import models
from django.utils.crypto import get_random_string


class SlugGenMixin:
    def generate_unique_slug(self, obj, slug_length=7):
        if not obj.slug:
            obj.slug = get_random_string(slug_length)
            
            slug_is_bad = True
            while slug_is_bad:
                slug_is_bad = False
                other_objs_with_slug = type(obj).objects.filter(slug=obj.slug)
                if len(other_objs_with_slug) > 0:
                    # if any other objects have current slug
                    slug_is_bad = True
                    obj.slug = get_random_string(slug_length)
