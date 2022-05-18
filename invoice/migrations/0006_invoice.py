# Generated by Django 4.0.3 on 2022-05-18 11:36

from django.db import migrations, models
import django.db.models.deletion
import invoice.utils


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_name', models.CharField(blank=True, max_length=100, null=True)),
                ('invoice_no', models.CharField(blank=True, default=invoice.utils.invoice_no, editable=False, max_length=6, null=True, unique=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('payment_Terms', models.CharField(choices=[('1 Day', '1 Day'), ('7 Days', '7 Days'), ('14 Days', '14 Days'), ('21 Day', '21 Days')], default='1 Day', max_length=100)),
                ('status', models.CharField(choices=[('CURRENT', 'CURRENT'), ('OVERDUE', 'OVERDUE'), ('PAID', 'PAID')], default='CURRENT', max_length=100)),
                ('notes', models.TextField(blank=True, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='invoice.client')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='invoice.product')),
            ],
        ),
    ]