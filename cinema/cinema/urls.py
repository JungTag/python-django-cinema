"""cinema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import user.views
import staff.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user.views.main, name='main'),
    path('update/', user.views.update_DB, name='db'),
    path('genre/', user.views.make_genre, name='genre'),
    path('login/', user.views.login, name='login'),
    path('logout/', user.views.logout, name='logout'),
    path('signup/', user.views.signup, name='signup'),
    path('recommend/',user.views.recommend, name='recommend'),
    path('activate/<str:uidb64>/<str:token>/', user.views.activate, name="activate"),
    path('vote/<int:movie_id>/', user.views.vote, name="vote"),
    path('detail/<int:movie_id>', user.views.detail, name='detail'),
    path('total/', staff.views.total, name='total'),
    path('1/', staff.views.seoul, name='seoul'),
    path('2/', staff.views.north_gyeongi, name='north_gyeongi'),
    path('3/', staff.views.south_gyeongi, name='south_gyeongi'),
    path('4/', staff.views.incheon, name='incheon'),
    path('5/', staff.views.gangwon, name='gangwon'),
    path('6/', staff.views.daejeon, name='daejeon'),
    path('7/', staff.views.chungcheong, name='chungcheong'),
    path('8/', staff.views.daegu, name='daegu'),
    path('9/', staff.views.busan, name='busan'),
    path('10/', staff.views.ulsan, name='ulsan'),
    path('11/', staff.views.gyeongsang, name='gyeongsang'),
    path('12/', staff.views.gwangju, name='gwangju'),
    path('13/', staff.views.jeonra, name='jeonra'),
    path('14/', staff.views.jeju, name='jeju'),
    path('staff_main/', staff.views.staff_main, name='staff_main'),
    path('re_release/<int:movie_id>', user.views.re_release, name='re_release'),
    path('deletion/<int:movie_id>', user.views.deletion, name="deletion")
]
