# Generated by Django 5.0.4 on 2024-05-01 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('last', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=12)),
                ('addres', models.TextField()),
                ('liter', models.IntegerField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
