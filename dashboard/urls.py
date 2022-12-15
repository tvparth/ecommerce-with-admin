from django.urls import path,re_path
from dashboard import views
from .views import admin_login, register_user
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    
    path('custom/',admin_login,name='admin'),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('dashboard/', views.index, name='home'),
    path('user/',views.show_user,name='user'),
    path('tables/',views.show_product,name='table'),
    path('add_product/',views.add_product,name='insert'),
    path('<int:id>/',views.update_product,name='update'),
    path('delete/<int:id>/',views.delete_data,name='delete'),
    
    
    re_path(r'^.*\.*', views.pages, name='pages'),
    
    
    
 



]