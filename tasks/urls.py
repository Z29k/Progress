from django.conf.urls import urls
from tasks import views

urlpatterns = [
	url(r'^$', views.task_list)
	url(r'^(?P<pk>[0-9]+)/$', views.task_detail)
]