# Generated by Django 4.2.3 on 2023-08-31 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contec',
            old_name='emil',
            new_name='email',
        ),
    ]
