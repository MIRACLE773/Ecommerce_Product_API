"""
URL configuration for ecommerce_product_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from ecommerce_product_api.views import home  # <-- add this

urlpatterns = [
    path('admin/', admin.site.urls),

    # API endpoints
    path('', home, name='home'),
    path('api/accounts/', include('accounts.urls')),   # auth endpoints
    path('api/products/', include('products.urls')),   # product endpoints
    path('api/orders/', include('orders.urls')),       # order & cart endpoints
    path("api/cart/", include("cart.urls")),           # cart endpoints
]

# Serve static & media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
