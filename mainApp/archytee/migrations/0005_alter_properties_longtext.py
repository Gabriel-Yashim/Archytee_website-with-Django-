# Generated by Django 4.2.7 on 2023-11-13 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archytee', '0004_properties_slide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='LongText',
            field=models.TextField(max_length=2000),
        ),
    ]
