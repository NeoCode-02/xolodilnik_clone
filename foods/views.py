from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

class ShopView(TemplateView):
    template_name = "shop.html"

class ProductSingleView(TemplateView):
    template_name = "product-single.html"

class AboutView(TemplateView):
    template_name = "about.html"

class BlogView(TemplateView):
    template_name = "blog.html"

class BlogSingleView(TemplateView):
    template_name = "blog-single.html"

class ContactView(TemplateView):
    template_name = "contact.html"

class CartView(TemplateView):
    template_name = "cart.html"

class WishlistView(TemplateView):
    template_name = "wishlist.html"

class CheckoutView(TemplateView):
    template_name = "checkout.html"
