# Generated by Django 4.0.3 on 2022-03-05 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='customer_name',
            field=models.CharField(help_text='enter customer name', max_length=50, verbose_name='custome name'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='total_sum',
            field=models.FloatField(default=2.0),
        ),
    ]
