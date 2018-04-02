from django.conf.urls import url
from . import views

app_name = 'viewer'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^by_folder/$', views.by_folder, name='by_folder'),
    url(r'^by_withsubs/$', views.by_withsubs, name='by_withsubs'),
    url(r'^by_withoutsubs/$', views.by_withoutsubs, name='by_withoutsubs'),
    url(r'^refresh_list/$', views.refresh_list, name='refresh_list'),
    url(r'^detail/(?P<m_detail>.+?)/$', views.detail_view, name='detail_view'),
    url(r'^delete/(?P<d_file>.+?)/$', views.delete_file, name='delete_view'),
    url(r'^download-subtitle/(?P<f_name>.+?)/$', views.download_view, name='download_view'),
]