from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
# Create your views here.
from django.views import View
from orders.forms import CartAddForm
from utils import IsAdminUsermixin
from .forms import PostSearchForm
from .models import Product, Category
from . import tasks


class HomeView(View):
    form_class = PostSearchForm

    def get(self, request, category_slug=None):
        forms = CartAddForm()
        products = Product.objects.filter(available=True)
        categories = Category.objects.filter(is_sub=False)
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category)
        if request.GET.get('search'):
            products = products.filter(body__contains=request.GET['search'])
        return render(request, 'home/home.html', {'products': products,
                                                  'categories': categories, 'form': self.form_class, 'forms': forms})
    #
    # def post(self, request):
    #     images =


# class HomeView(TemplateView):
#     template_name = 'home/home.html'
#
#     def get_context_data(self, category_slug=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['products'] = Product.objects.filter(available=True)
#         context['categories'] = Category.objects.filter(is_sub=False)
#         if category_slug:
#             context['category'] = Category.objects.get(slug=category_slug)
#             context['products'] = context['products'].filter(category=context['category'])
#         return context


class ProductDetileView(View):
    def get(self, request, slug, category_slug=None):
        form = CartAddForm()
        product = get_object_or_404(Product, slug=slug)
        products = Product.objects.filter(available=True)
        categories = Category.objects.filter(is_sub=False)
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'home/detile.html', {'product': product, 'form': form, 'products': products,
                                                    'categories': categories})


#
# class ProductDetileView(DetailView):
#     model = Product
#     template_name = 'home/detile.html'
#     context_object_name = 'product'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = CartAddForm()
#         return context


class BucketHome(IsAdminUsermixin, View):
    template_name = 'home/bucket.html'

    def get(self, request):
        objects = tasks.all_objects_tasks
        return render(request, self.template_name, {'objects': objects})


class DeleteBucketObject(IsAdminUsermixin, View):
    def get(self, request, key):
        tasks.delete_obj_bucket_task.delay(key)
        messages.success(request, 'your object will be delete soon', 'info')
        return redirect('home:bucket')


class DownloadBucketObject(IsAdminUsermixin, View):
    def get(self, request, key):
        tasks.download_obj_bucket_task(key)
        messages.success(request, 'your object will be download soon', 'info')
        return redirect('home:bucket')


class HomeContactView(View):
    def get(self, request, category_slug=None):
        products = Product.objects.filter(available=True)
        categories = Category.objects.filter(is_sub=False)
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'home/contact.html', {'products': products,
                                                     'categories': categories})

