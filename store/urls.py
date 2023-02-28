from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('category/<slug:slug>/', CategoryList.as_view(), name='category_detail'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
    path('new/', ProductCreateView.as_view(), name="new"),
    path('edit/<int:pk>/', ProductUpdate.as_view(), name="edit"),

    # Registration url
    path("login_registration/", login_registration, name="login_registration"),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),

    # pass
    path('save_review/<int:product_id>/', save_review, name='save_review'),
    path('add-favourite/<slug:product_slug>/', save_favourite_product, name='add_favourite'),
    path('my_favourite/', FavouriteProductView.as_view(), name='favourite_products'),
    path('save_email/', save_email, name='save_email'),
    path('send_mail/', send_mail_to_customers, name='send_mail'),

    # Korzinka url
    path('cart/', cart, name='cart'),
    path('to_card/<int:product_id>/<str:action>/', to_cart, name="to_card"),
    path('checkout/', checkout, name="checkout"),
    path('clear/', clear_cart, name='clear'),

    # Payment url
    path('payment/', create_checkout_sessions, name='payment'),
    path('payment_success/', successPayment, name='success'),
]
