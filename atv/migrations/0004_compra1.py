# Generated by Django 4.1.1 on 2022-09-17 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atv', '0003_rename_nome_compra_peca'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peca', models.CharField(max_length=100)),
                ('cor', models.CharField(max_length=50)),
            ],
        ),
    ]
