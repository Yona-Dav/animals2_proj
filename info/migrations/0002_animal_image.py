# Generated by Django 3.2.9 on 2021-11-22 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='image',
            field=models.ImageField(default=None, upload_to=''),
            preserve_default=False,
        ),
    ]
