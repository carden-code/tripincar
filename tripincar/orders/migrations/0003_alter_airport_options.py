# Generated by Django 4.1.1 on 2022-11-04 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="airport",
            options={"verbose_name": "Аэропорт", "verbose_name_plural": "Аэропорты"},
        ),
    ]
