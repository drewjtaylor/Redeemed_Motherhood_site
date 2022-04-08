# Generated by Django 3.1.1 on 2022-04-08 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_added_due_date_to_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoices',
            name='owing_client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='invoices',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
