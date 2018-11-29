from django.shortcuts import render

from django.http import HttpResponse
from .models import Product, Category, SubCategory
from django.template import loader

import json

def index(request):

    prod_list = list()

    for p in Product.objects.all():
        prod = dict(prod_id   = p.product_id,
                    prod      = p.product_name, 
                    category = p.category_name.category_name,
                    sub_cat  = p.sub_category.sub_category_name)

        prod_list.append(prod)
		
    template = loader.get_template('products/index.html')
    context = {
        'prod_list':prod_list,
    }

    return HttpResponse(template.render(context, request))
    #return HttpResponse(json.dumps(prod_list))
    

	
def get_products(request):

    products = [dict( id = p.product_id,
	                  prod     = p.product_name, 
                      category = p.category_name.category_name,
                      sub_cat  = p.sub_category.sub_category_name) for p in Product.objects.all()]

    #return HttpResponse(json.dumps(dict(data=products)))
    return HttpResponse(json.dumps(products))
    
	
	
	
def table(request):

    	
    template = loader.get_template('list_view.html')
    

    return HttpResponse(template.render(request))
    
	


def get_categories(request):

    categories = [cat.category_name for cat in Category.objects.all()]

    return HttpResponse(json.dumps(categories))




def get_sub_categories(request, category):

    sub_cat_objects = SubCategory.objects.filter(category_name__category_name__iexact=category )

    sub_categories = [cat.sub_category_name for cat in sub_cat_objects]
    
    return HttpResponse(json.dumps(sub_categories))



def product_for_category(request, category):

    product_objects = Product.objects.filter(category_name__category_name__iexact=category )

    prod_list = [prod.product_name for prod in product_objects]
    
    return HttpResponse(json.dumps(prod_list))




def product_for_sub_category(request, sub_category):

    product_objects = Product.objects.filter(sub_category__sub_category_name__iexact=sub_category)

    prod_list = [prod.product_name for prod in product_objects]
    
    return HttpResponse(json.dumps(prod_list))




def add_product(request, prod_name, sub_category, category):

    
    
    new_prod = Product( product_name  = prod_name,
                        category_name = Category.objects.filter(category_name__iexact=category)[0],
                        sub_category  = SubCategory.objects.filter(sub_category_name__iexact=sub_category)[0])
					   
    new_prod.save()
	
    product_objects = Product.objects.filter( sub_category__sub_category_name__iexact=sub_category,
										category_name__category_name__iexact=category )
										
    prod_list = [prod.product_name for prod in product_objects]
        
    return HttpResponse(json.dumps(prod_list))







