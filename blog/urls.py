from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^blog/', views.post_list, name='post_list')
]