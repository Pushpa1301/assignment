# Generated by Django 4.2.3 on 2023-08-31 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_emil_contec_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contec',
            name='content',
            field=models.TextField(),
        ),
    ]
