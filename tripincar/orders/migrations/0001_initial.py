# Generated by Django 4.1.1 on 2022-11-04 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Airport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128, verbose_name="Аэропорт")),
                (
                    "start_price",
                    models.IntegerField(verbose_name="Стартовая стоимость"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        choices=[
                            ("Рязань", "Рязань"),
                            ("Тула", "Тула"),
                            ("Владимир", "Владимир"),
                        ],
                        default="",
                        max_length=128,
                        verbose_name="Город",
                    ),
                ),
                ("address", models.CharField(max_length=256, verbose_name="Адрес")),
                (
                    "flight_number",
                    models.CharField(max_length=16, verbose_name="Номер рейса"),
                ),
                ("date", models.DateField(verbose_name="Дата подачи авто")),
                ("time", models.TimeField(verbose_name="Время подачи авто")),
                ("departure_time", models.TimeField(verbose_name="Время вылета")),
                ("telephone", models.CharField(max_length=11, verbose_name="Телефон")),
                (
                    "comment",
                    models.TextField(
                        blank=True, max_length=256, verbose_name="Комментарий"
                    ),
                ),
                (
                    "price",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Стоимость"
                    ),
                ),
                (
                    "status",
                    models.BooleanField(default=False, verbose_name="Статус заказа"),
                ),
                (
                    "pub_date",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="Дата публикации"
                    ),
                ),
                (
                    "update_date",
                    models.DateTimeField(
                        auto_now=True, db_index=True, verbose_name="Дата обновления"
                    ),
                ),
                (
                    "airport",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="orders.airport",
                        verbose_name="Аэропорт",
                    ),
                ),
            ],
            options={
                "verbose_name": "Заказ",
                "verbose_name_plural": "Заказы",
                "ordering": ("-pub_date",),
            },
        ),
    ]
