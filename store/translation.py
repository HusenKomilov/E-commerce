from modeltranslation.translator import translator, TranslationOptions, register
from .models import Product, Category


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'parent')


class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'category')


translator.register(Product, ProductTranslationOptions)
# translator.register(Category, CategoryTranslationOptions)
