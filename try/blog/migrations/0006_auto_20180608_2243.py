# Generated by Django 2.0.6 on 2018-06-08 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180608_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
