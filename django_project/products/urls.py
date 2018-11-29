from django.conf.urls import url

from . import views

urlpatterns = [
        
            url(r'/sub_categories/for_category=([A-Za-z]+)/$', views.get_sub_categories),          
            url(r'/for_category/([A-Za-z]+)/$', views.product_for_category),          
            url(r'/for_sub_category/([A-Za-z]+)/$', views.product_for_sub_category),          
			url(r'/add/([A-Za-z]+)/([A-Za-z]+)/([A-Za-z]+)/$', views.add_product),          
            url('/categories', views.get_categories), 
            url('/get_products', views.get_products), 			
            url('/list', views.index, name='index'),
			url('/viewTable', views.table, name='table'),
			
        ]

