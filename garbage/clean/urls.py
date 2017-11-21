from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^next$',views.next, name='next'),
   url(r'^store/(?P<city>\w+)/(?P<latitude>\d+\.\d+)/(?P<longitude>\d+\.\d+)/(?P<sens1>\d+)/(?P<sens2>\d+)/(?P<sens3>\d+)/',views.store,name="store"),
   url(r'^results$',views.results, name='results'),
   url(r'^Location$',views.Location,name ='Location'),
   ]
