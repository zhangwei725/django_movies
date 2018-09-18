from django.conf.urls import url

from home import views

urlpatterns = [
    url('detail/(\w+)/', views.detail, name='detail')
]
