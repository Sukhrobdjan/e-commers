# Generated by Django 4.2 on 2023-04-30 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id']},
        ),
    ]
