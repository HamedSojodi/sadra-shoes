# Generated by Django 4.0.5 on 2022-07-10 09:26

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=colorfield.fields.ColorField(blank=True, choices=[('#FFFFFF', 'white'), ('#000000', 'black')], default=None, image_field=None, max_length=18, null=True, samples=None),
        ),
    ]