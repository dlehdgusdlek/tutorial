# Generated by Django 2.2.5 on 2022-01-18 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0003_armyshop'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='armyshop',
            options={'managed': False},
        ),
        migrations.AlterModelTable(
            name='armyshop',
            table='army_shop',
        ),
    ]
