"""textutils URL Configuration

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
from django.urls import path
from . import views

# ------------------------------TUT  2 3 4------------
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.index,name='index'),
#     path('About',views.About,name='About'),
# # --------------------------------------------------------------TUT 5-----------------------------------
#     path('tut5',views.tut5,name='tut5'),
# # ----------------------------------------------------------------TUT 6----------------------------------
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('tut6',views.tut6,name='tut6')
# ]
# --------------------------------------------------------------TUT  7-------------------------------------------

#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.tut7,name='tut7'),
#     path('removepunc',views.removepunc,name='removepunc'),
#     path('capitalizefirst',views.capitalizefirst,name='capitalizefirst'),
#     path('newlineremove',views.newlineremove,name='newlineremove'),
#     path('spaceremove',views.spaceremove,name='spaceremove'),
#     path('charcount', views.charcount, name='charcount')
#
# ]

# --------------------------------------------------------------TUT 8------------------------------------------
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.index,name='index'),
#     path('removepunc',views.removepunc,name='removepunc'),
#     path('capitalizefirst',views.capitalizefirst,name='capitalizefirst'),
#     path('newlineremove',views.newlineremove,name='newlineremove'),
#     path('spaceremove',views.spaceremove,name='spaceremove'),
#     path('charcount', views.charcount, name='charcount')
#
# ]
# -------------------------------------------------------TUT  9-------------------------
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.index,name='index'),
#     path('removepunc',views.removepunc,name='removepunc'),
#     path('capitalizefirst',views.capitalizefirst,name='capitalizefirst'),
#     path('newlineremove',views.newlineremove,name='newlineremove'),
#     path('spaceremove',views.spaceremove,name='spaceremove'),
#     path('charcount', views.charcount, name='charcount')
#
# ]
# ---------------------------------------------------------TUT 10-------------------------------------
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.index,name='index'),
#     path('analyze',views.analyze,name='analyze')
# ]

# -----------------------------------------------------------------TUT 11---------------------------
# EXERCISE 1 SOLUTION   TUT 6

# -------------------------------------------------------------TUT 12 --------------------------------
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.index,name='index'),
#     path('analyze',views.analyze,name='analyze')
# ]

# ----------------------------------------------------------------TUT 13 ------------------------------------

# THIS IS EXERCISE


# -------------------------------------------------------------------TUT 14-------------------------------------


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('analyze',views.analyze,name='analyze')
]
