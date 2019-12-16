"""EcommerceWebsite URL Configuration

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
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from django.conf import settings


from home.views import home_screen_view
from account.views import signup_view, logout_view, signin_view
from shop.views import ShopView, ProductView, add_to_cart_view, cart_view, remove_from_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name="home"),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('signin/', signin_view, name='signin'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('shop/', ShopView.as_view(), name='shop'),
    path('product/<slug>/', ProductView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart_view, name='add-to-cart'),
    path('cart/', cart_view, name='cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)