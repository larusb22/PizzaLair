# Generated by Django 4.2 on 2023-05-11 22:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0005_delete_order'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_unregistereduser_rename_countries_country_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('profile_image', models.CharField(max_length=9999)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='unregistereduser',
            name='address',
        ),
        migrations.RemoveField(
            model_name='useraddress',
            name='country',
        ),
        migrations.DeleteModel(
            name='AccountUser',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='UnregisteredUser',
        ),
        migrations.DeleteModel(
            name='UserAddress',
        ),
    ]
