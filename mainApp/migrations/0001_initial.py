# Generated by Django 4.1.4 on 2023-07-12 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('addressline1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('addressline2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('addressline3', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pin', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('city', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('state', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('pic', models.FileField(blank=True, default='noimage.jpg', null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.IntegerField()),
                ('shipping', models.IntegerField()),
                ('final', models.IntegerField()),
                ('mode', models.CharField(default='COD', max_length=20)),
                ('orderstatus', models.IntegerField(choices=[(0, 'Cancel'), (1, 'Not Packed'), (2, 'Packed'), (3, 'Out for Delivery'), (4, 'Delivered')], default=1)),
                ('paymentstatus', models.IntegerField(choices=[(1, 'Pending'), (2, 'Done')], default=1)),
                ('rppid', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('rpoid', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('rpsid', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.buyer')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Done')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Maincategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Newslater',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('baseprice', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('finalprice', models.IntegerField()),
                ('size', models.CharField(max_length=150)),
                ('color', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('stock', models.CharField(default='In Stock', max_length=20)),
                ('pic1', models.ImageField(blank=True, default='noimagep.jpg', null=True, upload_to='images')),
                ('pic2', models.ImageField(blank=True, default='noimagep.jpg', null=True, upload_to='images')),
                ('pic3', models.ImageField(blank=True, default='noimagep.jpg', null=True, upload_to='images')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.brand')),
                ('maincategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.maincategory')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('addressline1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('addressline2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('addressline3', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pin', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('city', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('state', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('pic', models.FileField(blank=True, default='noimage.jpg', null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.buyer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.seller'),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.subcategory'),
        ),
        migrations.CreateModel(
            name='CheckoutProducts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('total', models.IntegerField()),
                ('pic', models.FileField(blank=True, default='noimage.jpg', null=True, upload_to='images')),
                ('checkout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.checkout')),
            ],
        ),
    ]
