# Generated by Django 4.2.17 on 2025-01-10 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectornote',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]