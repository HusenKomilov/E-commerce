from django import template
from store.models import Category, FavouriteProducts

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.filter(parent=None)


@register.simple_tag()
def get_sorted():
    sortes = [
        {
            'title': "Narxi bo'yicha",
            'sorters': [
                ('price', "O'sish bo'yicha"),
                ('-price', "Kamayish bo'yicha")
            ]
        },
        {
            'title': "Rangi bo'yicha",
            'sorters': [
                ('color', "A dan Z gacha"),
                ('-color', "Z dan A gacha")
            ]
        },
        {
            'title': "Razmeri bo'yicha",
            'sorters': [
                ('size', "O'shish bo'yicha"),
                ('-size', "Kamayish bo'yicha")
            ]
        }
    ]
    return sortes


@register.simple_tag()
def get_subcategories(category):
    return Category.objects.filter(parent=category)


# @register.simple_tag()
# def get_favourite_products(user):
#     fav = FavouriteProducts.objects.filter(user=user)
#     products = [i.product for i in fav]
#     return products
@register.simple_tag()
def get_fav_products(user):
    fav = FavouriteProducts.objects.filter(user=user)
    product = [i.product for i in fav]
    return product
