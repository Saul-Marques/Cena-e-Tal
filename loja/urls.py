from django.urls import path, include
from loja.views.products import produto_detail, fazer_licitacao
from loja.views.home import Index
from loja.views.login import Login
from loja.views.signup_email import SignupEmailCheck
from loja.views.signup_continue import SignupContinue
from loja.views.products import produto_detail
from loja.views.categoria import CategoriaView
from loja.views.user import UserView
from loja.views.logout import logout_view  
from loja.views.contactos import contactos_view
from loja.views.upload_product import upload_product_view

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('login/', Login.as_view(), name='login'),
    path("signup/email/", SignupEmailCheck.as_view(), name="signup_email"),
    path("signup/continue/", SignupContinue.as_view(), name="signup_continue"),
    path('produto/<int:id>/', produto_detail, name='produto_detail'),
    path('licitacao/<int:id>/', fazer_licitacao, name='fazer_licitacao'),    
    path('categoria/', CategoriaView.as_view(), name='categorias'),
    path('user/<int:user_id>/', UserView.as_view(), name='user'),
    path('logout/', logout_view, name='logout'),
    path('contactos/', contactos_view, name='contactos'),  
    path("upload-product/", upload_product_view, name="upload_product"),
    ]
