from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from shop.models import Product, Category
from cart.forms import QuantityForm


def paginat(request, list_objects):
	p = Paginator(list_objects, 20)
	page_number = request.GET.get('page')
	try:
		page_obj = p.get_page(page_number)
	except PageNotAnInteger:
		page_obj = p.page(1)
	except EmptyPage:
		page_obj = p.page(p.num_pages)
	return page_obj


def home_page(request):
	products = Product.objects.all()
	context = {'products': paginat(request ,products)}
	return render(request, 'home_page.html', context)


def product_detail(request, id):
	form = QuantityForm()
	try:

		product = get_object_or_404(Product, id=id)
		related_products = Product.objects.filter(category=product.category).all()[:5]
		context = {
			'title':product.title,
			'product':product,
			'form':form,
			'favorites':'favorites',
			'related_products':related_products
		}
		
		if request.user.likes.filter(id=product.id).first():
			context['favorites'] = 'remove'
	except:
		return redirect('accounts:user_login')
	return render(request, 'product_detail.html', context)


@login_required
def add_to_favorites(request, product_id):
	product = get_object_or_404(Product, id=product_id)
	request.user.likes.add(product)
	return redirect('shop:product_detail', id=product_id)


@login_required
def remove_from_favorites(request, product_id):
	product = get_object_or_404(Product, id=product_id)
	request.user.likes.remove(product)
	return redirect('shop:favorites')


@login_required
def favorites(request):
	products = request.user.likes.all()
	context = {'title':'Favorites', 'products':products}
	return render(request, 'favorites.html', context)




def about_page(request):
	
	
	return render(request, 'about_page.html')


def search(request):
	query = request.GET.get('q')
	products = Product.objects.filter(title__icontains=query).all()
	context = {'products': paginat(request ,products)}
	return render(request, 'home_page.html', context)


def filter_by_category(request, id):
    category = get_object_or_404(Category, id=id)

    # Initialize result list for products
    result = Product.objects.filter(category=category)

    # Log the result for debugging purposes
    print('result', result)

    # Paginate the result
    context = {'products': paginat(request, result)}
    return render(request, 'home_page.html', context)
