from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register('users', UserListAPIVIew, basename='users')
router.register('mail', MailAPIViewSets, basename='mail')
urlpatterns = [
    path('products/', product_list_api_view),
    path('category/', CategoryListAPIView.as_view()),
    path('products/<int:pk>/', ProductDetailAPIView.as_view()),
    path('gallary/<int:pk>/', gallary_list_api_view),
    path('review/', ReviewAPIView.as_view()),
] + router.urls
