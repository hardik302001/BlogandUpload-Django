# Generated by Django 3.0.7 on 2021-03-16 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210316_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumb',
            field=models.ImageField(null=True, upload_to='media/images'),
        ),
    ]
