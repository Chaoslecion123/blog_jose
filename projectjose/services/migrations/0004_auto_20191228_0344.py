# Generated by Django 2.0.9 on 2019-12-28 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20191228_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(default='', upload_to='services'),
            preserve_default=False,
        ),
    ]
