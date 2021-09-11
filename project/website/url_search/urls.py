from django.urls import path

from . import views


urlpatterns = [
        path('',views.home, name='showlist'),
        path('add',views.add, name='add'),
        path('website_search/', views.website_search, name='website_search')
]