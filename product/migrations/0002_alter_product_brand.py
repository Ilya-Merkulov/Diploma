# Generated by Django 4.0.4 on 2022-05-15 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='product.brand'),
            preserve_default=False,
        ),
    ]
