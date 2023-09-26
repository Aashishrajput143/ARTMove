# Generated by Django 4.1.4 on 2023-08-21 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_blog_excert_blog_explain_blog_pic1_blog_pic2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='brand',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mainApp.brand'),
        ),
        migrations.AddField(
            model_name='services',
            name='maincategory',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mainApp.maincategory'),
        ),
        migrations.AddField(
            model_name='services',
            name='subcategory',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mainApp.subcategory'),
        ),
    ]