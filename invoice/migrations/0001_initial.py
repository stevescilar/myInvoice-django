# Generated by Django 4.0.3 on 2022-05-19 07:15

from django.db import migrations, models
import django.db.models.deletion
import invoice.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientName', models.CharField(blank=True, max_length=200, null=True)),
                ('phone_number', models.CharField(max_length=50, null=True, unique=True)),
                ('email', models.EmailField(max_length=100, null=True, unique=True)),
                ('logo', models.ImageField(blank=True, upload_to='brandname')),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('unit_price', models.FloatField(blank=True, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientName', models.CharField(blank=True, max_length=200, null=True)),
                ('phone_number', models.CharField(max_length=50, null=True, unique=True)),
                ('email', models.EmailField(max_length=100, null=True, unique=True)),
                ('logo', models.ImageField(blank=True, upload_to='brandname')),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
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
