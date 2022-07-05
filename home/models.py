from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django_resized import ResizedImageField

class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='scategory',
                                     null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:category_filter', args=[self.slug, ])

@receiver(pre_save, sender=Category)
def my_handler(sender, instance, *args, **kwargs):
    slug = slugify(instance.name)
    exists = Category.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s"%(slug, instance.id)
    instance.slug =slug


class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='products')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    image = ResizedImageField(size=[1000, 1000])
    description = RichTextField()
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:product_detile', args=[self.slug, ])


@receiver(pre_save, sender=Product)
def my_handler(sender, instance, *args, **kwargs):
    slug = slugify(instance.name)
    exists = Product.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s"%(slug, instance.id)
    instance.slug =slug
