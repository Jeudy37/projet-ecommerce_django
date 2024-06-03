from django.urls import path

from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('categories', views.categories, name='categories'),
    path('products', views.products, name='products'),
    path('category/delete/<int:id>', views.delete_category, name='delete_category'),
    path('products/delete/<int:id>', views.delete_product, name='delete_product'),
    path('products/edit/<int:id>', views.edit_product, name='edit_product'),
     path('categories/edit/<int:id>', views.edit_categori, name='edit_categori'),
    path('orders', views.orders, name='orders'),
    path('orders/detail/<int:id>', views.order_detail, name='order_detail'),
    path('orders/confirm/<int:order_id>/', views.order_confirm, name='order_confirm'),
    path('orders/cancel/<int:order_id>/', views.order_cancel, name='order_cancel'),
    path('add-product/', views.add_product, name='add_product'),
    path('add-category/', views.add_category, name='add_category'),
]
