# Generated by Django 4.1.1 on 2022-09-17 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cor', models.CharField(max_length=50)),
            ],
        ),
    ]