from django.urls import path
from store import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, PasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
urlpatterns = [

    # View Urls
    path('', views.ProductView.as_view(),name='home'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    
    # Cart Url
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart,),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),

    
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    
    # Login And Registration Url
    path('accounts/login/',auth_views.LoginView.as_view
    (template_name ='store/login.html',authentication_form=LoginForm),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page = 'login'),name='logout'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),


    # Password Change Url
    path('changepassword/',auth_views.PasswordChangeView.as_view(template_name ='store/passchange.html',
    form_class = PasswordChangeForm, success_url='/changepassdone/' ), name='passwordchange'),
    path('changepassdone/',auth_views.PasswordChangeDoneView.as_view(
        template_name ='store/passchangedone.html'),name='passwordchangedone'),
    path('password-reset/',auth_views.PasswordResetView.as_view(
        template_name ='store/pass_reset.html',form_class=MyPasswordResetForm),name="password-reset"),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(
        template_name ='store/pass_reset_done.html'),name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(
        template_name ='store/pass_reset_confirm.html',
        form_class =MySetPasswordForm),name="password_reset_confirm"),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(
        template_name ='store/pass_reset_complete.html'),name="password_reset_complete"),
   
    
    # Filter Url
    path('leptop/', views.leptop, name='leptop'),
    path('leptop/<slug:data>', views.leptop, name='leptopdata'),

    # Order And PayMent Url
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)