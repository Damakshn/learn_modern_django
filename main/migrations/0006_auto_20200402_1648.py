# Generated by Django 3.0.4 on 2020-04-02 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_productname_capitalize'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttag',
            name='products',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, to='main.ProductTag'),
        ),
    ]
