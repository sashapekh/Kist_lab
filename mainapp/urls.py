from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^search_form/$', views.search_form , name='search_form'),
    url(r'^result/$',views.result, name='result')

]
