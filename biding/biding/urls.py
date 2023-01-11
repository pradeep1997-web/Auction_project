
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('bidportal', views.bidportal, name='bidportal'),
    path('auction/<int:pk>',views.auction,name='auction'),
    path('bid/<int:pk>', views.bidfun, name='bid'),
    path('register', views.register, name='register'),
    path('loginf', views.loginf, name='loginf'),
    path('logoutf', views.logoutf, name='logoutf'),
    path('result', views.result, name='result')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

