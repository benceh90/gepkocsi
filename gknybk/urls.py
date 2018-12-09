from django.urls import path

from . import views

urlpatterns = [
    # ex: /index/5/
    path('', views.index, name='index'),
    # ex: /index/5/
    path('rogzites/', views.rogzites, name='rogzites'),

]
