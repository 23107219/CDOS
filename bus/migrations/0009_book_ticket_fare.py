# Generated by Django 2.2.6 on 2019-12-15 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0008_auto_20191215_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_ticket',
            name='fare',
            field=models.IntegerField(null=True),
        ),
    ]
