# Generated by Django 4.1.7 on 2023-03-24 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invtry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
