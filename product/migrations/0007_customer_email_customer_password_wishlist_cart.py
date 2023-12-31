# Generated by Django 4.2.7 on 2023-12-08 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_customer_seller_email_seller_password_seller_pincode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='No email', max_length=254),
        ),
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default='No password', max_length=100),
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.customer')),
                ('products', models.ManyToManyField(to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.customer')),
                ('products', models.ManyToManyField(to='product.product')),
            ],
        ),
    ]
