# Generated by Django 3.2.16 on 2023-03-07 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='url',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]