# Generated by Django 4.0 on 2024-11-04 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0003_alter_address_deleted_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interests',
            name='deleted_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
