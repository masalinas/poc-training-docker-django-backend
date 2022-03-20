from django.contrib import admin
from django.urls import re_path
from ApiApplication import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/products$', views.product_list),
    #re_path(r'^api/products/(?P<pk>[0-9]+)$', views.product_detail)
    re_path(r'^api/products/(?P<pk>[-\w]+)$', views.product_detail)
]
