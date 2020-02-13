from django import forms
from .models import ClassifiedAd
from django.utils import translation
from django.utils.translation import ugettext as _

translation.activate('ru')


class ClassifiedAdCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user_language = 'ru'
        translation.activate(user_language)
        #request.session[translation.LANGUAGE_SESSION_KEY] = user_language

        super().__init__(*args, **kwargs)

        #Dirty hack
        #TODO: fix it - find the way to localize labels properly
        self.fields['region'].label = 'Регион'  #_('region')
        self.fields['category'].label = 'Категория' #_('category')
        self.fields['header'].label = 'Заголовок' #_('header')
        self.fields['body'].label = 'Текст сообщения' #_('body')
        self.fields['price'].label = 'Цена' #_('price')
        self.fields['image'].label = 'Изображение' #_('image')

    class Meta:
        model = ClassifiedAd
        

        fields = ['region',
              'category',
              'header',
              'body',
              'price',
              'image',
            ]

        localized_fields = ['region',
              'category',
              'header',
              'body',
              'price',
              'image',
            ]