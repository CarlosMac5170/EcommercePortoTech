"""EcommercePorto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from core import views as core
from usuario import views as usuario
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', core.home, name='home'),
    path('about/', core.about, name='about'),
    path('admin/', admin.site.urls),

#----------------------------------- Users ------------------------------------------------------
    path('login/', usuario.login, name='signIn'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', usuario.register, name='register'),

#----------------------------------- Products ------------------------------------------------------
    path('productos/', include('producto.urls', namespace='producto')),
    path('carrito/', include('cart.urls', namespace='cart')),
    path('order/', include('orden.urls', namespace='order'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)