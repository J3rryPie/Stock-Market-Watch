# Generated by Django 3.1.4 on 2021-06-16 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='script',
            name='buy_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='script',
            name='buy_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='script',
            name='change',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='script',
            name='change_percentage',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='script',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='script',
            name='sell_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='script',
            name='sell_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='script',
            name='state',
            field=models.CharField(default='un', max_length=2),
        ),
    ]
