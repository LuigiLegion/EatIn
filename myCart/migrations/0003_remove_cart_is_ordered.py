# Generated by Django 2.2.4 on 2019-09-30 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myCart', '0002_auto_20190928_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='is_ordered',
        ),
    ]