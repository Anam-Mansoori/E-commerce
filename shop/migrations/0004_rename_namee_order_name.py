# Generated by Django 3.2.3 on 2021-06-26 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210626_1643'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='namee',
            new_name='name',
        ),
    ]