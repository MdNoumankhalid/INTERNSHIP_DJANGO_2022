"""intership URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.templatetags.static import static
from django.urls import path
from intership_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('reg',views.reg,name='reg'),
    path('reg_view',views.reg_view,name='reg_view'),
    path('login',views.login,name='login'),
    path('CustomerOrder',views.CustomerOrder,name='CustomerOrder'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('addproduct_view',views.addproduct_view,name='addproduct_view'),
    path('reg_del/<int:pk>',views.reg_del,name='reg_del'),
    path('reg_edit/<int:pk>',views.reg_edit,name='reg_edit'),
    path('category',views.category,name='category'),
    path('category_view',views.category_view,name='category_view'),
    path('cat_edit/<int:pk>',views.cat_edit,name='cat_edit'),
    path('forgotpass',views.forgotpass,name='forgotpass'),
    path('otp',views.otp,name='otp'),
    path('resetpass',views.resetpass,name='resetpass'),
    path('product_del/<int:pk>',views.product_del,name='product_del'),
    path('product_edit/<int:pk>',views.product_edit,name='product_edit'),
    path('product_view_user',views.product_view_user,name='product_view_user'),
    path('cat_wise_products/<str:cat>',views.cat_wise_products,name='cat_wise_products'),
    path('cat_del/<int:pk>',views.cat_del,name='cat_del'),
    path('add_cart/<int:pk>',views.add_cart,name='add_cart'),
    path('my_cart',views.my_cart,name='my_cart'),
    path('remove_cart/<int:pk>', views.remove_cart, name='remove_cart'),
    path('confirm_order/<int:pk>', views.confirm_order, name='confirm_order'),
    path('my_order',views.my_order,name='my_order'),
    path('payment/<int:pk>', views.payment, name='payment'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

















