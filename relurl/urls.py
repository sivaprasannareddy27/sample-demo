from django.conf.urls import url
from relurl import views 

app_name='relurl'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^other/',views.other,name='other'),
    url(r'^relurls/',views.rel_url,name='rel_url')
]
