# Generated by Django 5.1 on 2024-09-20 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0062_defaultvalues_invoice_account_holder_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="BankDetail",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("account_holder_name", models.CharField(max_length=100)),
                ("account_number", models.CharField(max_length=16)),
                ("sort_code", models.CharField(max_length=9)),
            ],
        ),
        migrations.AddField(
            model_name="defaultvalues",
            name="bank_details",
            field=models.ManyToManyField(blank=True, related_name="default_values", to="backend.bankdetail"),
        ),
    ]
