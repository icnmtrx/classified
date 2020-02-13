"""
Docstring
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import (ListView, DetailView, CreateView, 
UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.translation import ugettext_lazy as _

from .models import Category, ClassifiedAd
from .forms import ClassifiedAdCreateForm

from users.models import Profile

from django.utils import translation

translation.activate('ru')

# Create your views here.
class CatListMixin():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        active_ads = ClassifiedAd.objects.filter(active=True)
        all_categories = Category.objects.all()

#        empty_count = active_ads.filter(category__isnull=True).count()

        categories_count = [] #[ {'cat': 'empty', 'count':empty_count} ]
        

        for cat in all_categories:
            items_in_cat = active_ads.filter(category=cat).count()
            categories_count.append({ 'cat': cat, 'count': items_in_cat})
        
        context['categories_count'] = categories_count
        return context


class DefaultView(ListView):
    template_name = 'classified/home.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super(DefaultView, self).get_context_data(**kwargs)

        active_ads = ClassifiedAd.objects.filter(active=True)
        all_categories = Category.objects.all()

#        empty_count = active_ads.filter(category__isnull=True).count()

        categories_count = [] #[ {'cat': 'empty', 'count':empty_count} ]
        

        for cat in all_categories:
            items_in_cat = active_ads.filter(category=cat).count()
            categories_count.append({ 'cat': cat, 'count': items_in_cat})
        
        context['categories_count'] = categories_count
        return context


class ClassifiedAdsView(CatListMixin, ListView):
    model = ClassifiedAd
    template_name = 'classified/adv_list.html'
    paginate_by = 10
    #slug_url_kwarg = 'cat'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.request.GET.get('cat', None)
        
        if category is None:
            #dirty hack
            #TODO: make it localized
            context['title'] = 'Все объявления'
        else:
            objects = Category.objects.filter(slug=category)
            if objects is not None and len(objects) > 0:
                context['title'] = objects[0].title
        
        return context


    def get_queryset(self):
        category = self.request.GET.get('cat', None)
        print('cat', category)
        if category is None:
            qs = ClassifiedAd.objects.all().order_by('-date_posted')
        else:
            qs = ClassifiedAd.objects.filter(category__slug=category).order_by('-date_posted')
        return qs

class ClassifiedAdView(CatListMixin, DetailView):
    model = ClassifiedAd
    template_name = 'classified/adv_detail.html'
    slug_url_kwarg = 'adv'
    context_object_name = 'object'
    
class ClassifiedAdAuthorView(CatListMixin, ListView):
    model = ClassifiedAd
    template_name = 'classified/adv_author.html'

    def get_queryset(self):
        author = self.kwargs.get('author')
        objects = ClassifiedAd.objects.filter(author__slug=author).order_by('-date_posted', 'active')
        return objects
        
    def get_context_data(self, **kwargs):
        context = super(ClassifiedAdAuthorView, self).get_context_data(**kwargs)

        active_author = self.kwargs.get('author')
        author = get_object_or_404(Profile, slug=active_author)
        
        context['author'] = author
        return context



class ClassifiedAdCreateView(LoginRequiredMixin, CreateView):
    #model = ClassifiedAd
    template_name = 'classified/adv_create.html'
    # fields = ['region',
    #           'category',
    #           'header',
    #           'body',
    #           'price',
    #           'image',
    #         ]
    form_class = ClassifiedAdCreateForm
    user_language = 'ru'
    translation.activate(user_language)
    #request.session[translation.LANGUAGE_SESSION_KEY] = user_language


    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class ClassifiedAdUpdateView(CatListMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ClassifiedAd
    template_name = 'classified/adv_create.html'
    fields = ['region',
              'category',
              'header',
              'body',
              'price',
              'image',
            ]
    class Meta:
        localized_fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

    def test_func(self):
        adv = self.get_object()
        if self.request.user.profile == adv.author:
            return True
        return False


class ClassifiedAdDeleteView(CatListMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ClassifiedAd
    success_url = '/'
    template_name = 'classified/adv_confirm_delete.html'

    def test_func(self):
        adv = self.get_object()
        if self.request.user.profile == adv.author:
            return True
        return False