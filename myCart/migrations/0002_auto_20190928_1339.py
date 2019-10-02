# Generated by Django 2.2.4 on 2019-09-28 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
        ('myCart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='is_ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='order',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='payment.Order'),
        ),
    ]