# Generated by Django 3.2.13 on 2022-07-19 08:23

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_product_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, '37'), (2, '38'), (3, '39'), (4, '40'), (4, '41'), (4, '42'), (4, '43'), (5, '44')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, '37'), (2, '38'), (3, '39'), (4, '40'), (4, '41'), (4, '42'), (4, '43'), (5, '44')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
