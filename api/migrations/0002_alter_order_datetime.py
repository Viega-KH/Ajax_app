# Generated by Django 5.0.4 on 2024-05-01 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
