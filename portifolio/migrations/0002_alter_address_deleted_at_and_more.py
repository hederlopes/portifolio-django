# Generated by Django 4.0 on 2024-11-04 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='deleted_at',
            field=models.DateTimeField(default=False),
        ),
        migrations.AlterField(
            model_name='complementary_courses',
            name='deleted_at',
            field=models.DateTimeField(default=False),
        ),
        migrations.AlterField(
            model_name='contact',
            name='deleted_at',
            field=models.DateTimeField(default=False),
        ),
        migrations.AlterField(
            model_name='education',
            name='deleted_at',
            field=models.DateTimeField(default=False),
        ),
        migrations.AlterField(
            model_name='experience',
            name='deleted_at',
            field=models.DateTimeField(default=False),
        ),
        migrations.AlterField(
            model_name='interests',
            name='deleted_at',
            field=models.DateTimeField(default=False),
        ),
        migrations.AlterField(
            model_name='skills',
            name='deleted_at',
            field=models.DateTimeField(default=False),
        ),
    ]