from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_viwe
from .forms import LoginForm
from .forms import MyPasswordResetForm, MyPasswordChangeForm

urlpatterns = [
    path('', views.home),
    path('about/', views.about,name="about"),
    path('contact/', views.contact, name="contact"),
    path('category/<slug:val>', views.CategoryView.as_view(), name="category"),
    path('category-title/<val>', views.CategoryTitle.as_view(), name="category-title"),
    path('productdetail/<int:pk>', views.ProductDetail.as_view(), name="product-detail"),
    path('profile/', views.profileViwe.as_view(), name="profile"),
    path('address/', views.address, name="address"),
    path('updateaddress/<int:pk>', views.updateAddress.as_view(), name="updateAddress"),
   

   #login authentication

   path('registration/',views.CustomerRegistrationViwe.as_view(), name="customerregistration"),
   path('accounts/login/',auth_viwe.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name="login"),
   path('password_reset/',auth_viwe.PasswordResetView.as_view
        (template_name='app/password_reset.html', form_class= MyPasswordResetForm) ,name="password_reset"),
   path('passwordchange/',auth_viwe.PasswordChangeView.as_view
        (template_name='app/changepassword.html',form_class=MyPasswordChangeForm, success_url ='/passwordchangedone'), name="passwordchange"),
    path('passwordchangedone/',auth_viwe.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name="passwordchangedone"),
    path('logout/',auth_viwe.LogoutView.as_view(next_page='login'), name="logout"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)