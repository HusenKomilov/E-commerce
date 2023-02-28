from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# mahsulot kategoriyasi
class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="Kategoriyalar")
    image = models.ImageField(upload_to='categories/', verbose_name="Kategoriya Rasmi", null=True, blank=True)
    slug = models.SlugField(unique=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Kategoriya",
                               related_name="subcategories")

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def get_image(self):
        if self.image:
            return self.image
        else:
            return "data:image/png;base64,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"

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Category: pk={self.pk}, title: {self.title}"

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


# mahsulotlar
class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name="Mahsulot nomi")
    prise = models.FloatField(verbose_name="Narxi")
    created_add = models.DateTimeField(auto_now_add=True, verbose_name="Saytga chiqarilgan vaqti")
    quantity = models.IntegerField(default=0, verbose_name="Mahsulotlar soni")
    description = models.TextField(blank=True, default="Tez orada bu yerda mahsulot bo'ladi",
                                   verbose_name="Batafsil ma'lumot")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriya", related_name="products")
    slug = models.SlugField(unique=True, null=True)
    size = models.IntegerField(default=30, verbose_name="mm dagi o'lchami")
    color = models.CharField(max_length=30, default="Kumush", verbose_name="Rangi/Materiali")

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    # imglar
    def get_first_photo(self):
        if self.images:
            try:
                return self.images.first().image.url
            except:
                return "data:image/png;base64,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"
        else:
            return "data:image/png;base64,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"

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Mahsulot: pk={self.pk}, title={self.title}"

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"


# rasmlar uchun
class Gallery(models.Model):
    image = models.ImageField(upload_to='products/', verbose_name='Rasm')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")

    class Meta:
        verbose_name = "Rasm"
        verbose_name_plural = "Mahsulotlar gallareyasi"


# komentariyalar
class Review(models.Model):
    text = models.TextField(verbose_name="Izoh matni")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.username

    class Meta:
        verbose_name = "Izohlar"
        verbose_name_plural = "Izohlar"


# tanlangan mahsulotlar
class FavouriteProducts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Tanlangan mahsulot")

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = "Tanlangan mahsulot"
        verbose_name_plural = "Tanlangan mahsulotlar"


# email saqlash
class Mail(models.Model):
    mail = models.EmailField(unique=True, verbose_name='Email kiritadigan maydon')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.mail

    class Meta:
        verbose_name = 'Pochta'
        verbose_name_plural = 'Pochtalar addresi'


# xaridor
class Customers(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=255, verbose_name='Xaridor ismi')
    last_name = models.CharField(max_length=255, verbose_name='Elektron manzil')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Xaridor'
        verbose_name_plural = 'Xaridorlar'


class Order(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    shipping = models.BooleanField(default=True)

    def __str__(self):
        return str(self.pk) + ' '

    class Meta:
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'Buyurtmalar'

    @property
    def get_cart_total_price(self):
        order_products = self.orderproduct_set.all()
        total_price = sum([product.get_total_prise for product in order_products])
        return total_price

    @property
    def get_cart_total_quantity(self):
        order_products = self.orderproduct_set.all()
        total_quantity = sum([product.quantity for product in order_products])
        return total_quantity


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Buyurtma tovari'
        verbose_name_plural = 'Buyurtma tovarlari'

    @property
    def get_total_prise(self):
        total_price = self.product.prise * self.quantity
        return total_price


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255)
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name="Shaharlar")
    state = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Адрес доставки'
        verbose_name_plural = 'Адреса доставки'


class City(models.Model):
    city_name = models.CharField(max_length=255, verbose_name='Shaharlar nomi')

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name = "Shahar"
        verbose_name_plural = "Shaharlar"
