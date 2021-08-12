"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from blog import views
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('accounts/login/',LoginView.as_view(), name="login"),
    # path('accounts/login/',views.login,name="login"),
    path('accounts/logout/',LogoutView.as_view(),name="logout",kwargs={'next_page':'/' }),
]
# from django.conf.urls import url, include
# from django.contrib import admin
# from django.contrib.auth.views import LoginView,LogoutView
#
# # from . import views
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'', include('blog.urls')),
#     url(r'^accounts/login/$',LoginView.as_view(), name='login'),
#     url(r'^accounts/logout/$',LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
# ]
