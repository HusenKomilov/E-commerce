from rest_framework import serializers
from store.models import Category, Product, Review, Mail, Gallery
from django.contrib.auth import get_user_model


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'parent', 'image')


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class GallarySerializers(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('id', 'image', 'product')


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'author', 'product', 'created_at')


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email')


class MailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = ('id', 'mail', 'user')
