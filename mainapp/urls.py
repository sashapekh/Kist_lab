from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^search_form/$', views.search_form, name='search_form'),
    url(r'^result/$', views.result, name='result'),
    url(r'^result_qur_2', views.result_qur_2, name='result_qur_2'),
    url(r'^result_3_query', views.result_3_query, name='result_3_query'),
    url(r'^result_4_query', views.result_4_query, name='result_4_query'),

]
