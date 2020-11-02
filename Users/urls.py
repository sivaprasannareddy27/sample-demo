from django.conf.urls import url
from Users import views
urlpatterns = [
    url(r'^$',views.form_view,name='formview'),
    
]