# Generated by Django 4.2.7 on 2023-12-05 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='user',
        ),
        migrations.AddField(
            model_name='seller',
            name='user_name',
            field=models.CharField(default='No Company', max_length=100),
        ),
    ]
