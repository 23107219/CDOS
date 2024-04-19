# Generated by Django 2.2.6 on 2019-12-14 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0002_add_bus_add_route_book_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_bus',
            name='trevaltime',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=30, null=True)),
                ('fare', models.IntegerField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bus.Register')),
            ],
        ),
    ]
