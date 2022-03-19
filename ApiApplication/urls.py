from django.urls import re_path
from ApiApplication import views

urlpatterns = [
    re_path(r'^api/products$', views.product_list),
    re_path(r'^api/products/(?P<pk>[0-9]+)$', views.product_detail),
    re_path(r'^api/products/published$', views.product_list_published)
]
