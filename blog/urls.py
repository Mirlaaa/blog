"""blog URL Configuration

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
from django.urls import path
from postagem.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name="index"),
    path('informatica/',informatica, name="informatica"),
    path('noticia/', noticia, name="noticia"),
    path('alimentos/',alimentos,name="alimentos"),
    path('apicultura/',apicultura,name="apicultura"),
    path('quimica/',quimica,name="quimica"),
    path('ads/',ads,name="ads"),
    path('agroindustria/',agroindustria,name="agroindustria")
]
