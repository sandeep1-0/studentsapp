from django.conf.urls import url
from students import views

urlpatterns = [
    url(r'^registration$',views.Registration,name='registration'),
    url(r'^$',views.Login,name='login'),
    url(r'^detailform$',views.detailform, name='details'),
    url(r'^dash$',views.dashboard,name='dash'),
    url(r'^logout$',views.logout),
    url(r'^update',views.update),
    url(r'^delete',views.delete),
    url(r'^students',views.viewall,name='students'),
    ]
