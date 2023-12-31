# Generated by Django 4.2.6 on 2023-10-28 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consumer',
            old_name='default_currency_id',
            new_name='default_currency',
        ),
        migrations.RenameField(
            model_name='costgroup',
            old_name='consumer_id',
            new_name='consumer',
        ),
        migrations.RenameField(
            model_name='costrecord',
            old_name='consumer_id',
            new_name='consumer',
        ),
        migrations.RenameField(
            model_name='costrecord',
            old_name='currency_id',
            new_name='currency',
        ),
    ]
