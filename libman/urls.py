from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.index, name='index'),
    url(r'^(?P<bookisbn>[0-9-]+)/$',views.details, name='details'),
    url(r'^delete/$',views.delete,name='delete'),
    url(r'^edit/$',views.edit,name='edit'),
    url(r'^add_book/$',views.add_book,name='add_book'),
    url(r'^add_author/$',views.add_author,name='add_author'),
]