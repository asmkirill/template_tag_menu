from django.urls import re_path
from tree.views import IndexView


app_name = 'tree'


urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),
    re_path(r'^(.*)/$', IndexView.as_view(), name='index'),
]
