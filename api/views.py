from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from store.models import Category, Product, Review, Mail, User
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAdminUser


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


@api_view(['GET'])
def product_list_api_view(request):
    product = Product.objects.all()
    serializers = ProductSerializers(product, many=True)
    context = {
        'status': 200,
        'data': serializers.data
    }
    return Response(context)


@api_view(['GET'])
def gallary_list_api_view(request):
    gallary = Gallery.objects.all()
    serializers = GallarySerializers(gallary, many=True)
    context = {
        'status': 200,
        'data': serializers.data
    }
    return Response(context)


class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Product
    serializer_class = ProductSerializers


class ReviewAPIView(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request):
        review = Review.objects.all()
        serializers = ReviewSerializers(review, many=True)
        context = {
            'status': 200,
            'data': serializers.data
        }
        return Response(context)


class UserListAPIVIew(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializers


class MailAPIViewSets(viewsets.ModelViewSet):
    queryset = Mail.objects.all()
    serializer_class = MailSerializers

