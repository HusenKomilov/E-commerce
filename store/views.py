from random import randint
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Category, Review, FavouriteProducts, Mail
from .forms import LoginForm, RegistrationForm, ReviewForm, CustomerForms, ShippingForms, ProductForm
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .utils import *
from blogs import settings
from django.urls import reverse
import stripe


class ProductList(ListView):
    model = Product
    context_object_name = 'categories'

    extra_context = {
        'title': "Totembo bosh sahifasi"
    }
    template_name = 'store/product_list.html'

    def get_queryset(self):
        categories = Category.objects.filter(parent=None)
        return categories


class CategoryList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'store/category_page.html'
    paginate_by = 4

    def get_queryset(self):
        sort_field = self.request.GET.get('sort')
        type_field = self.request.GET.get('type')
        if type_field:
            products = Product.objects.filter(category__slug=type_field)
            return products
        main_category = Category.objects.get(slug=self.kwargs['slug'])
        subcategories = main_category.subcategories.all()
        products = Product.objects.filter(category__in=subcategories)

        if sort_field:
            products = products.order_by(sort_field)
        return products

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        main_category = Category.objects.get(slug=self.kwargs['slug'])
        context['category'] = main_category
        context['title'] = f"Kategoriya {main_category.title}"
        return context


class ProductDetail(DetailView):
    model = Product
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        product = Product.objects.get(slug=self.kwargs['slug'])

        context['title'] = f"Mahsulot {product.title}"
        products = Product.objects.all()
        data = []
        for i in range(4):
            random_p = randint(0, len(products) - 1)
            p = products[random_p]
            if p not in data:
                data.append(p)
        context['products'] = data
        context['reviews'] = Review.objects.filter(product=product)
        # if self.request.user.is_authenticated():
        context['review_form'] = ReviewForm()
        return context


def login_registration(request):
    context = {
        "title": "Kirish yoki roýxatdan o'tish",
        "login_form": LoginForm(),
        "registration_form": RegistrationForm()
    }
    return render(request, "store/login_registration.html", context)


def user_login(request):
    form = LoginForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect("product_list")
    else:
        messages.error(request, "Noto'g'ri")
        return redirect("login_registration")


def user_logout(request):
    logout(request)
    return redirect("product_list")


def register(request):
    form = RegistrationForm(data=request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Yaxshi")
    else:
        for field in form.errors:
            messages.error(request, form.errors[field].as_text())

    return redirect("login_registration")


def save_review(request, product_id):
    form = ReviewForm(data=request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.author = request.user
        review.product_id = product_id
        review.save()

    else:
        pass

    product = Product.objects.get(pk=product_id)
    return redirect('product_detail', product.slug)


# @login_required
def save_favourite_product(request, product_slug):
    user = request.user if request.user.is_authenticated else None
    product = Product.objects.get(slug=product_slug)
    favourite_products = FavouriteProducts.objects.filter(user=user)
    if user:
        if product in [i.product for i in favourite_products]:
            fav_product = FavouriteProducts.objects.get(user=user, product=product)
            fav_product.delete()
        else:
            FavouriteProducts.objects.create(user=user, product=product)
    next_page = request.META.get('HTTP_REFERER', 'product_list')
    return redirect(next_page)


class FavouriteProductView(LoginRequiredMixin, ListView):
    model = FavouriteProducts
    context_object_name = 'products'
    template_name = 'store/favourite_product.html'
    login_url = 'login_registration'

    def get_queryset(self):
        user = self.request.user
        favourite = FavouriteProducts.objects.filter(user=user)
        products = [i.product for i in favourite]
        return products


def save_email(request):
    email = request.POST.get('email')
    user = request.user if request.user.is_authenticated else None
    if email:
        try:
            Mail.objects.create(mail=email, user=user)
        except:
            pass
            # messages.success(request, 'ASSDASASD')
    next_page = request.META.get('HTTP_REFERER', 'product_list')
    return redirect(next_page)


def send_mail_to_customers(request):
    from blogs import settings
    from django.core.mail import send_mail
    if request.method == 'POST':
        text = request.POST.get('text')
        mail_list = Mail.objects.all()
        for email in mail_list:
            mail = send_mail(
                subject='Sizga uchun yangi aksiya!',
                message=text,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False
            )
            print(f"Jonatildimi? {email} -- {bool(mail)}")

    else:
        pass
    return render(request, 'store/send_mail.html')


def cart(request):
    '''Korzinka'''
    cart_info = get_cart_data(request)

    context = {
        'cart_total_quantity': cart_info['cart_total_quantity'],
        'order': cart_info['order'],
        'products': cart_info['products']
    }

    return render(request, 'store/card.html', context)


def to_cart(request, product_id, action):
    '''Koorzinkaga tovar qo'shish'''
    if request.user.is_authenticated:
        user_cart = CartForAuthenticatedUser(request, product_id, action)
        return redirect('cart')
    else:
        print("ERROOORRRR")
        messages.error(request, "Xaridni amalga oshirish uchun, Avtorizatsoyadan yoki ro'yxatdan o'ting!")
        return redirect('login_registration')


def checkout(request):
    cart_info = get_cart_data(request)
    context = {
        'cart_total_quantity': cart_info['cart_total_quantity'],
        'order': cart_info['order'],
        'items': cart_info['products'],
        "customer_form": CustomerForms,
        "shipping_form": ShippingForms,
        "title": "Buyurtma berish"
    }
    return render(request, 'store/checkout.html', context)


"""Bu yerda to'lov tizimi ishlaydi"""


def create_checkout_sessions(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        user_cart = CartForAuthenticatedUser(request)
        cart_info = user_cart.get_cart_info()

        total_price = cart_info['cart_total_price']
        total_quantity = cart_info['cart_total_quantity']
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'En-Shop mahsulotlari'
                    },
                    'unit_amount': int(total_price) * 100
                },
                'quantity': total_quantity
            }, ],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('success')),
            cancel_url=request.build_absolute_uri(reverse('success'))
        )
        return redirect(session.url, 303)


def successPayment(request):
    user_cart = CartForAuthenticatedUser(request)
    user_cart.clear()
    messages.success(request, "To'lov muvofaqiyatli amalga oshirildi")
    return render(request, 'store/success.html')


def clear_cart(request):
    user_cart = CartForAuthenticatedUser(request)
    order = user_cart.get_cart_info()['order']
    order_products = order.orderproduct_set.all()

    for order_product in order_products:
        quantity = order_product.quantity
        product = order_product.product
        order_product.delete()
        product.quantity += quantity
        product.save()

    return redirect('product_list')


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'store/new_product.html'


class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'store/new_product.html'
