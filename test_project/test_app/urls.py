from django.conf.urls import url
from test_app import views


urlpatterns = [
    url('',views.users,name='users'),
]
