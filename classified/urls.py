from django.urls import path
from . import views as classified_views

#app_name = 'classified'

urlpatterns = [
     #path('', classified_views.DefaultView.as_view(), 
     #    name='classified-home'),
     #path('list/', 
     #    classified_views.ClassifiedAdsView.as_view(), 
     #    name='adv-list'),
    path('', 
         classified_views.ClassifiedAdsView.as_view(), 
         name='classified-home'),
     path('', 
         classified_views.ClassifiedAdsView.as_view(), 
         name='adv-list'),

# #   path('content/<category>/<slug>/',
# #        views.ClassifiedAdView.as_view(template_name='classified/adv_detail.html'), 
# #        name='classified-ad'),
     path('detail/<slug:adv>/',
         classified_views.ClassifiedAdView.as_view(), 
         name='adv-detail'),
     path('author/<author>/',
         classified_views.ClassifiedAdAuthorView.as_view(), 
         name='adv-author-list'),
     path('msg/create-new/', 
          classified_views.ClassifiedAdCreateView.as_view(), 
          name='adv-create'),
     path('msg/<slug>/update/', 
          classified_views.ClassifiedAdUpdateView.as_view(), 
          name='adv-update'),
     path('msg/<slug>/delete/', 
          classified_views.ClassifiedAdDeleteView.as_view(), 
          name='adv-delete'),
]