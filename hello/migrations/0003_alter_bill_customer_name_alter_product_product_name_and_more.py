# Generated by Django 4.0.2 on 2022-03-12 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_alter_bill_customer_name_alter_bill_total_sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='customer_name',
            field=models.CharField(max_length=50, verbose_name='Custome Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=50, verbose_name='Product Name'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='category_name',
            field=models.CharField(help_text='enter category name', max_length=50, verbose_name='Category Name'),
        ),
        migrations.CreateModel(
            name='bill_product',
            fields=[
                ('bill_product_num', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=1, help_text='default is 1')),
                ('bill_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hello.bill')),
                ('billprod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hello.product')),
            ],
        ),
        migrations.AlterField(
            model_name='bill',
            name='products',
            field=models.ManyToManyField(to='hello.bill_product'),
        ),
    ]